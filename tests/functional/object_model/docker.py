#
# Copyright (c) 2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time
from typing import List

import docker
from retry.api import retry_call

import config
from utils.parametrization import get_ports_for_fixture
from utils.files_operation import save_container_logs_to_file
from utils.logger import get_logger
import utils.mtls as mtls

logger = get_logger(__name__)
CONTAINER_STATUS_RUNNING = "running"
TERMINAL_STATUSES = ["exited"]


class Docker:
    
    COMMON_RETRY = {"tries": 90, "delay": 2}
    GETTING_LOGS_RETRY = COMMON_RETRY
    GETTING_STATUS_RETRY = COMMON_RETRY

    def __init__(self, request, container_name, start_container_command,
                 env_vars_container=None, image=config.image, container_log_line=config.container_log_line):
        self.client = docker.from_env()
        self.grpc_port, self.rest_port = get_ports_for_fixture()
        self.image = image
        self.container = None
        self.request = request
        self.container_name = container_name
        self.start_container_command = start_container_command
        self.env_vars_container = env_vars_container if env_vars_container else []
        self.container_log_line = container_log_line

    def start(self):

        def finalizer():
            if self.container is not None:
                self.save_container_logs()
                self.container.stop()
                self.container.remove()

        self.request.addfinalizer(finalizer)

        volumes_dict = {'{}'.format(config.path_to_mount): {'bind': '/opt/ml',
                                                            'mode': 'ro'} }
        if mtls.is_enabled() and 'minio' not in self.image:
            print("========= ENABLED ===========" * 20)
            mtls_volumes_dict = mtls.get_mtls_keychain().docker_py_volumes_dict()
            self.image += '-nginx-mtls'
            volumes_dict = {**volumes_dict, **mtls_volumes_dict}

        self.container = self.client.containers.run(image=self.image, detach=True,
                                                    name=self.container_name,
                                                    ports={'{}/tcp'.format(self.grpc_port):
                                                               self.grpc_port,
                                                           '{}/tcp'.format(self.rest_port):
                                                               self.rest_port},
                                                    volumes=volumes_dict,
                                                    command=self.start_container_command,
                                                    environment=self.env_vars_container)
        print("!!!"*20)
        from pprint import pprint
        pprint(self.image)
        pprint(self.start_container_command) #  environment=self.env_vars_container)
        self.ensure_container_status(status=CONTAINER_STATUS_RUNNING, terminal_statuses=TERMINAL_STATUSES)
        self.ensure_logs_contains()
        return self.container, {"grpc_port": self.grpc_port, "rest_port": self.rest_port}

    def save_container_logs(self):
        if config.log_level == "DEBUG" and config.artifacts_dir != "":
            logs = self.container.logs().decode()
            save_container_logs_to_file(container=self.container, logs=logs)

    def ensure_logs(self):
        logs = str(self.container.logs())
        assert self.container_log_line in logs

    def ensure_logs_contains(self):
        return retry_call(self.ensure_logs, exceptions=AssertionError, **Docker.GETTING_LOGS_RETRY)

    def get_container_status(self):
        container = self.client.containers.get(self.container.id)
        return container.status

    def ensure_status(self, status, terminal_statuses=None):
        current_status = self.get_container_status()
        if terminal_statuses is not None and current_status in terminal_statuses:
            raise RuntimeError("Received terminal status '{}' for container {}".format(current_status,
                                                                                       self.container_name))
        assert current_status == status, \
            "Not expected status for container {} found. \n " \
            "Expected: {}, \n " \
            "received: {}".format(self.container.name, status, self.container.status)

    def ensure_container_status(self, status: str = CONTAINER_STATUS_RUNNING,
                                terminal_statuses: List[str] = None):
        container_statuses = {"status": status}
        if terminal_statuses:
            container_statuses["terminal_statuses"] = terminal_statuses
        time.sleep(1)
        return retry_call(self.ensure_status, fkwargs=container_statuses,
                          exceptions=AssertionError, **Docker.GETTING_STATUS_RETRY)
