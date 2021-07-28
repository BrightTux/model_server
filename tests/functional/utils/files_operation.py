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
import os
import config
import datetime


def save_container_logs_to_file(container, logs, dir_path: str = config.artifacts_dir):
    time_stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    test_case = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
    test_case = "".join(list(map(lambda x: x if x.isalnum() else '_', test_case)))
    file_name = f"{container.name}_{test_case}_{time_stamp}.log"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)
    assert 0, f"{os.environ.get('PYTEST_CURRENT_TEST')}\n{file_name}"
    with open(file_path, "w+") as text_file:
        text_file.write(logs)
