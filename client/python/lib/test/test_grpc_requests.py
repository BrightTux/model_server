#
# Copyright (c) 2021 Intel Corporation
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

import pytest

from tensorflow_serving.apis.get_model_metadata_pb2 import GetModelMetadataRequest
from tensorflow_serving.apis.get_model_status_pb2 import GetModelStatusRequest

from ovmsclient.tfs_compat.grpc.requests import GrpcModelMetadataRequest, _check_model_spec, make_metadata_request, make_status_request, GrpcModelStatusRequest

from config import MODEL_SPEC_INVALID, MODEL_SPEC_VALID

@pytest.mark.parametrize("name, version", MODEL_SPEC_VALID)
def test_check_model_spec_valid(name, version):
    _check_model_spec(name, version)

@pytest.mark.parametrize("name, version, expected_exception, expected_message", MODEL_SPEC_INVALID)
def test_check_model_spec_invalid(name, version, expected_exception, expected_message):
    with pytest.raises(expected_exception) as e_info:
        _check_model_spec(name, version)
        assert str(e_info.value) == expected_message

@pytest.mark.parametrize("name, version", MODEL_SPEC_VALID)
def test_make_status_request_valid(mocker, name, version):
    mock_method = mocker.patch('ovmsclient.tfs_compat.grpc.requests._check_model_spec')
    model_status_request = make_status_request(name, version)

    mock_method.assert_called_once()
    assert isinstance(model_status_request, GrpcModelStatusRequest)
    assert model_status_request.model_version == version
    assert model_status_request.model_name == name
    assert isinstance(model_status_request.raw_request, GetModelStatusRequest)

@pytest.mark.parametrize("name, version, expected_exception, expected_message", MODEL_SPEC_INVALID)
def test_make_status_request_invalid(mocker, name, version, expected_exception, expected_message):
    mock_method = mocker.patch('ovmsclient.tfs_compat.grpc.requests._check_model_spec', side_effect=expected_exception(expected_message))
    with pytest.raises(expected_exception) as e_info:
        model_status_request = make_status_request(name, version)
        assert str(e_info.value) == expected_message
    mock_method.assert_called_once()

@pytest.mark.parametrize("name, version", MODEL_SPEC_VALID)
def test_make_metadata_request_vaild(mocker, name, version):
    mock_method = mocker.patch('ovmsclient.tfs_compat.grpc.requests._check_model_spec')
    model_metadata_request = make_metadata_request(name, version)

    mock_method.assert_called_once()
    assert isinstance(model_metadata_request, GrpcModelMetadataRequest)
    assert model_metadata_request.model_version == version
    assert model_metadata_request.model_name == name
    assert isinstance(model_metadata_request.raw_request, GetModelMetadataRequest)
    assert len(model_metadata_request.raw_request.metadata_field) == 1
    assert model_metadata_request.raw_request.metadata_field[0] == 'signature_def'

@pytest.mark.parametrize("name, version, expected_exception, expected_message", MODEL_SPEC_INVALID)
def test_make_metadata_request_invalid(mocker, name, version, expected_exception, expected_message):
    mock_method = mocker.patch('ovmsclient.tfs_compat.grpc.requests._check_model_spec', side_effect=expected_exception(expected_message))
    with pytest.raises(expected_exception) as e_info:
        model_metadata_request = make_metadata_request(name, version)
        assert str(e_info.value) == expected_message
    mock_method.assert_called_once()