#
# Copyright (c) 2020,2021 Intel Corporation
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
#config_setting(
#    name = "linux_distribution_family",
#    constraint_values = [
#        ":debian", # like Ubuntu
#        ":fedora", # like RHEL/CentOS
#    ],
#)

constraint_setting(name = "linux_distribution_family")
constraint_value(constraint_setting = "linux_distribution_family", name = "fedora") # like RHEL/CentOS
constraint_value(constraint_setting = "linux_distribution_family", name = "debian") # like Ubuntu

cc_library(
    name = "ovms_lib",
    linkstatic = 1,
    srcs = [
        "aliases.hpp",
        "blobmap.hpp",
        "config.cpp",
        "config.hpp",
        "custom_node.cpp",
        "custom_node.hpp",
        "custom_node_interface.h",
        "custom_node_library_manager.cpp",
        "custom_node_library_manager.hpp",
        "custom_node_output_allocator.hpp",
        "customnodesession.cpp",
        "customnodesession.hpp",
        "customloaderconfig.hpp",
        "customloaders.hpp",
        "customloaders.cpp",
        "customloaderinterface.hpp",
        "deserialization.cpp",
        "deserialization.hpp",
        "dl_node.cpp",
        "dl_node.hpp",
        "dlnodesession.cpp",
        "dlnodesession.hpp",
        "entry_node.cpp",
        "entry_node.hpp",
        "executingstreamidguard.hpp",
        "exit_node.cpp",
        "exit_node.hpp",
        "exitnodesession.cpp",
        "exitnodesession.hpp",
        "filesystem.hpp",
        "get_model_metadata_impl.cpp",
        "get_model_metadata_impl.hpp",
        "global_sequences_viewer.hpp",
        "global_sequences_viewer.cpp",
        "http_rest_api_handler.cpp",
        "http_rest_api_handler.hpp",
        "http_server.cpp",
        "http_server.hpp",
        "localfilesystem.cpp",
        "localfilesystem.hpp",
        "gathernodeinputhandler.cpp",
        "gathernodeinputhandler.hpp",
        "gcsfilesystem.cpp",
        "gcsfilesystem.hpp",
        "model.cpp",
        "model.hpp",
        "model_version_policy.cpp",
        "model_version_policy.hpp",
        "modelchangesubscription.cpp",
        "modelchangesubscription.hpp",
        "modelconfig.cpp",
        "modelconfig.hpp",
        "modelmanager.cpp",
        "modelmanager.hpp",
        "modelinstance.cpp",
        "modelinstance.hpp",
        "modelinstanceunloadguard.cpp",
        "modelinstanceunloadguard.hpp",
        "modelversion.hpp",
        "modelversionstatus.hpp",
        "model_service.hpp",
        "model_service.cpp",
        "node.cpp",
        "node.hpp",
        "nodeinfo.hpp",
        "node_library.cpp",
        "node_library.hpp",
        "node_library_utils.cpp",
        "node_library_utils.hpp",
        "nodesession.cpp",
        "nodesession.hpp",
        "nodesessionresult.hpp",
        "nodeinputhandler.cpp",
        "nodeinputhandler.hpp",
        "nodeoutputhandler.cpp",
        "nodeoutputhandler.hpp",
        "nodesessionmetadata.hpp",
        "nodesessionmetadata.cpp",
        "nodestreamidguard.hpp",
        "ovinferrequestsqueue.cpp",
        "ovinferrequestsqueue.hpp",
        "ov_utils.cpp",
        "ov_utils.hpp",
        "pipeline.cpp",
        "pipeline.hpp",
        "pipelinedefinition.cpp",
        "pipelinedefinition.hpp",
        "pipelinedefinitionstatus.hpp",
        "pipelinedefinitionunloadguard.cpp",
        "pipelinedefinitionunloadguard.hpp",
        "pipelineeventqueue.hpp",
        "pipeline_factory.cpp",
        "pipeline_factory.hpp",
        "prediction_service.cpp",
        "prediction_service.hpp",
        "prediction_service_utils.hpp",
        "prediction_service_utils.cpp",
        "sequence_processing_spec.hpp",
        "rest_parser.cpp",
        "rest_parser.hpp",
        "rest_utils.cpp",
        "rest_utils.hpp",
        "s3filesystem.cpp",
        "s3filesystem.hpp",
        "session_id.hpp",
        "shapeinfo.hpp",
        "statefulmodelinstance.cpp",
        "statefulmodelinstance.hpp",
        "azurestorage.hpp",
        "azurestorage.cpp",
        "azurefilesystem.cpp",
        "azurefilesystem.hpp",
        "serialization.cpp",
        "schema.hpp",
        "schema.cpp",
        "sequence.cpp",
        "sequence.hpp",
        "sequence_manager.cpp",
        "sequence_manager.hpp",
        "serialization.hpp",
        "server.cpp",
        "status.cpp",
        "status.hpp",
        "stringutils.hpp",
        "tensorinfo.cpp",
        "tensorinfo.hpp",
        "threadsafequeue.hpp",
        "timer.hpp",
        "version.hpp",
        "logging.hpp",
        "logging.cpp",
        "binaryutils.hpp",
        "binaryutils.cpp",
    ],
    deps = [
        "@tensorflow_serving//tensorflow_serving/apis:prediction_service_cc_proto",
        "@tensorflow_serving//tensorflow_serving/apis:model_service_cc_proto",
        "@com_github_grpc_grpc//:grpc++",
        "@org_tensorflow//tensorflow/core:framework",
        "@rapidjson//:rapidjson",
        "@spdlog//:spdlog",
        "@cxxopts//:cxxopts",
        "@awssdk//:s3",
        "@awssdk//:core",
        "@awssdk//:deps",
	    "@azure//:storage",
	    "@cpprest//:sdk",
	    "@boost//:lib",
        "@com_github_googleapis_google_cloud_cpp//google/cloud/storage:storage_client",
        "@tensorflow_serving//tensorflow_serving/util/net_http/server/public:http_server",
        "@tensorflow_serving//tensorflow_serving/util/net_http/server/public:http_server_api",
        "@tensorflow_serving//tensorflow_serving/util:threadpool_executor",
        "@tensorflow_serving//tensorflow_serving/util:json_tensor",
        "@openvino//:openvino",
        "@opencv//:opencv",
    ],
    local_defines = [
        "SPDLOG_ACTIVE_LEVEL=SPDLOG_LEVEL_DEBUG"
    ],
    copts = [
        "-Wall",
        "-Wno-unknown-pragmas",
        "-Werror",
        "-Wno-sign-compare",
    ],
)

cc_binary(
    name = "libsampleloader.so",
    srcs = [
	    "example/SampleCustomLoader/sampleCustLoader.cpp",
	    "customloaderinterface.hpp",
    ],
    linkshared = 1,
    deps = [
        "@rapidjson//:rapidjson",
    ],
)

cc_binary(
    name = "lib_node_mock.so",
    srcs = [
	    "test/custom_nodes/node_mock.c",
	    "custom_node_interface.h",
    ],
    linkshared = 1,
)

cc_binary(
    name = "lib_node_missing_implementation.so",
    srcs = [
	    "test/custom_nodes/node_missing_implementation.c",
	    "custom_node_interface.h",
    ],
    linkshared = 1,
)

cc_binary(
    name = "lib_node_add_sub.so",
    srcs = [
	    "test/custom_nodes/node_add_sub.c",
	    "custom_node_interface.h",
    ],
    linkshared = 1,
)

cc_binary(
    name = "lib_node_dynamic_image.so",
    srcs = [
	    "test/custom_nodes/node_dynamic_image.c",
	    "custom_node_interface.h",
    ],
    linkshared = 1,
)

cc_binary(
    name = "lib_node_choose_maximum.so",
    srcs = [
        "test/custom_nodes/node_choose_maximum.cpp",
        "custom_node_interface.h",
    ],
    linkshared = 1,
)
cc_binary(
    name = "lib_node_perform_different_operations.so",
    srcs = [
        "test/custom_nodes/node_perform_different_operations.cpp",
        "custom_node_interface.h",
    ],
    linkshared = 1,
)

cc_binary(
    name = "lib_node_dynamic_demultiplex.so",
    srcs = [
        "test/custom_nodes/node_dynamic_demultiplex.cpp",
        "custom_node_interface.h",
    ],
    linkshared = 1,
)

cc_binary(
    name = "libcustom_node_east_ocr.so",
    srcs = [
        "custom_nodes/east_ocr/east_ocr.cpp",
        "custom_nodes/east_ocr/utils.hpp",
        "custom_nodes/east_ocr/nms.hpp",
        "custom_node_interface.h",
    ],
    deps = [
        "@opencv//:opencv"
    ],
    linkshared = 1,
    copts = [
        "-Wall",
        "-Wno-unknown-pragmas",
        "-Werror"
    ]
)

cc_binary(
    name = "libcustom_node_model_zoo_intel_object_detection.so",
    srcs = [
        "custom_nodes/model_zoo_intel_object_detection/model_zoo_intel_object_detection.cpp",
        "custom_nodes/model_zoo_intel_object_detection/utils.hpp",
        "custom_node_interface.h",
    ],
    deps = [
        "@opencv//:opencv"
    ],
    linkshared = 1,
    copts = [
        "-Wall",
        "-Wno-unknown-pragmas",
        "-Werror"
    ]
)

cc_binary(
    name = "libcustom_node_image_transformation.so",
    srcs = [
        "custom_nodes/image_transformation/image_transformation.cpp",
        "custom_nodes/image_transformation/utils.hpp",
        "custom_node_interface.h",
    ],
    deps = [
        "@opencv//:opencv"
    ],
    linkshared = 1,
    copts = [
        "-Wall",
        "-Wno-unknown-pragmas",
        "-Werror"
    ]
)

cc_binary(
    name = "ovms",
    srcs = [
        "main.cpp",
    ],
    linkopts = [
        "-lxml2",
        "-luuid",
        "-lstdc++fs",
        "-lcrypto",
    ],
    copts = [
        "-Wconversion",
        "-Werror",
    ],
    deps = [
        "//src:ovms_lib",
    ]
)

cc_test(
    name = "ovms_test",
    linkstatic = 1,
    srcs = [
        "test/deserialization_tests.cpp",
        "test/ensemble_tests.cpp",
        "test/ensemble_flow_custom_node_tests.cpp",
        "test/ensemble_mapping_config_tests.cpp",
        "test/ensemble_metadata_test.cpp",
        "test/ensemble_config_change_stress.cpp",
        "test/gather_node_test.cpp",
        "test/demultiplexer_node_test.cpp",
        "test/get_model_metadata_response_test.cpp",
        "test/get_pipeline_metadata_response_test.cpp",
        "test/get_model_metadata_signature_test.cpp",
        "test/get_model_metadata_validation_test.cpp",
        "test/mockmodelinstancechangingstates.hpp",
        "test/mock_iinferrequest.hpp",
        "test/model_service_test.cpp",
        "test/model_version_policy_test.cpp",
        "test/model_test.cpp",
        "test/modelinstance_test.cpp",
        "test/modelconfig_test.cpp",
        "test/node_library_manager_test.cpp",
        "test/custom_node_output_allocator_test.cpp",
        "test/modelmanager_test.cpp",
        "test/ovmsconfig_test.cpp",
        "test/modelversionstatus_test.cpp",
        "test/localfilesystem_test.cpp",
        "test/gcsfilesystem_test.cpp",
        "test/azurefilesystem_test.cpp",
        "test/nodesessionmetadata_test.cpp",
        "test/ovtestutils.hpp",
        "test/ovinferrequestqueue_test.cpp",
        "test/ov_utils_test.cpp",
        "test/pipelinedefinitionstatus_test.cpp",
        "test/predict_validation_test.cpp",
        "test/prediction_service_test.cpp",
        "test/custom_loader_test.cpp",
        "test/binaryutils_test.cpp",
        "test/rest_parser_row_test.cpp",
        "test/rest_parser_column_test.cpp",
        "test/rest_parser_binary_inputs_test.cpp",
        "test/rest_parser_nonamed_test.cpp",
        "test/rest_utils_test.cpp",
        "test/sequence_test.cpp",
        "test/stateful_test_utils.hpp",
        "test/sequence_manager_test.cpp",
        "test/serialization_tests.cpp",
        "test/stateful_config_test.cpp",
        "test/stateful_modelinstance_test.cpp",
        "test/stringutils_test.cpp",
        "test/test_utils.cpp",
        "test/test_utils.hpp",
        "test/threadsafequeue_test.cpp",
        "test/unit_tests.cpp",
        "test/schema_test.cpp",
        "test/environment.hpp",
        "test/http_rest_api_handler_test.cpp",
    ],
    data = [
        "test/dummy/1/dummy.xml",
        "test/dummy/1/dummy.bin",
        "test/add_two_inputs_model/1/add.xml",
        "test/add_two_inputs_model/1/add.bin",
        "test/increment_1x3x4x5/1/increment_1x3x4x5.xml",
        "test/increment_1x3x4x5/1/increment_1x3x4x5.bin",
        "test/summator/1/summator.xml",
        "test/summator/1/summator.bin",
    ],
    linkopts = [
        "-lxml2",
        "-luuid",
        "-lstdc++fs",
        "-lcrypto",
        "-lssl",
    ],
    deps = [
        "//src:ovms_lib",
        "//src:libsampleloader.so",
        "//src:lib_node_mock.so",
        "//src:lib_node_missing_implementation.so",
        "//src:lib_node_add_sub.so",
        "//src:lib_node_dynamic_image.so",
        "//src:lib_node_dynamic_demultiplex.so",
        "//src:lib_node_perform_different_operations.so",
        "//src:lib_node_choose_maximum.so",
        "//src:libcustom_node_east_ocr.so",
        "//src:libcustom_node_model_zoo_intel_object_detection.so",
        "//src:libcustom_node_image_transformation.so",
        "@com_google_googletest//:gtest",
    ],
    copts = [
        "-Wall",
        "-Wno-unknown-pragmas",
        "-Werror",
    ],
)

filegroup(
  name = "static_analysis",
  srcs = [
    "//src:ovms",
    "//src:libcustom_node_east_ocr.so",
    "//src:libcustom_node_model_zoo_intel_object_detection.so",
    "//src:libcustom_node_image_transformation.so",
  ]
)
