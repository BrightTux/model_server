# Dynamic Shape with a Custom Node{#ovms_docs_dynamic_shape_custom_node}

## Introduction
This guide shows how to configure a simple Directed Acyclic Graph (DAG) with a custom node that performs input resizing before passing input data to the model. 

The node below is provided as a demonstration. See instructions for how to build and use the custom node: [Image Transformation](https://github.com/openvinotoolkit/model_server/tree/v2021.4.2/src/custom_nodes/image_transformation).


To run inference with this setup, we will use the following:

- Example client in Python [face_detection.py](https://github.com/openvinotoolkit/model_server/blob/v2021.4.2/example_client/face_detection.py) that can be used to request inference on with the desired input shape.

- An example [face_detection_retail_0004](https://docs.openvinotoolkit.org/2021.4/omz_models_model_face_detection_retail_0004.html) model.

When using the `face_detection_retail_0004` model with the `face_detection.py` script, images are loaded and resized to the desired width and height. Then the output from the server is processed and inference results are displayed with bounding boxes drawn around the detected faces. 

## Steps
Clone OpenVINO&trade; Model Server GitHub repository and enter `model_server` directory.
```
git clone https://github.com/openvinotoolkit/model_server.git
cd model_server
```

#### Download the Pretrained Model
Download the model files and store them in the `models` directory:
```Bash
mkdir -p models/face_detection/1
curl https://storage.openvinotoolkit.org/repositories/open_model_zoo/2021.4/models_bin/3/face-detection-retail-0004/FP32/face-detection-retail-0004.bin https://storage.openvinotoolkit.org/repositories/open_model_zoo/2021.4/models_bin/3/face-detection-retail-0004/FP32/face-detection-retail-0004.xml -o models/face_detection/1/face-detection-retail-0004.bin -o models/face_detection/1/face-detection-retail-0004.xml
```

#### Pull the Latest Model Server Image
Pull the latest version of OpenVINO&trade; Model Server from Docker Hub :
```Bash
docker pull openvino/model_server:latest
```

### Build a Custom Node

1. Go to the custom node directory:
    ```
    cd src/custom_nodes/image_transformation/
    ``` 

3. Build the custom node:
    ```
    make build
    ```

4. Copy the custom node to the `models` repository:
    ```
    cp lib/libcustom_node_image_transformation.so ../../../models
    ```

#### Create Model Server Configuration File
Go to the `models` directory:
```
cd ../../../models
```

Create a new file named `config.json` in the `models` directory:
```json
{
    "model_config_list": [
        {
            "config": {
                "name": "face_detection_retail",
                "base_path": "/models/face_detection",
            }
        }
    ],
    "custom_node_library_config_list": [
        {"name": "image_transformation",
            "base_path": "/models/libcustom_node_image_transformation.so"}
    ],
    "pipeline_config_list": [
        {
            "name": "face_detection",
            "inputs": ["image"],
            "nodes": [
                {
                    "name": "image_transformation_node",
                    "library_name": "image_transformation",
                    "type": "custom",
                    "params": {
                        "target_image_width": "300",
                        "target_image_height": "300",

                        "mean_values": "[123.675,116.28,103.53]",
                        "scale_values": "[58.395,57.12,57.375]",

                        "original_image_color_order": "BGR",
                        "target_image_color_order": "BGR",

                        "original_image_layout": "NCHW",
                        "target_image_layout": "NCHW",
                    },
                    "inputs": [
                        {"image": {
                                "node_name": "request",
                                "data_item": "image"}}],
                    "outputs": [
                        {"data_item": "image",
                            "alias": "transformed_image"}]
                },
                {
                    "name": "face_detection_node",
                    "model_name": "face_detection_retail",
                    "type": "DL model",
                    "inputs": [
                        {"input": 
                            {
                             "node_name": "image_transformation_node",
                             "data_item": "transformed_image"
                            }
                        }
                    ],
                    "outputs": [
                        {"data_item": "detection",
                         "alias": "face_detection_output"}
                    ]
                }
            ],
            "outputs": [
                {"detection": {
                        "node_name": "face_detection_node",
                        "data_item": "face_detection_output"}}
            ]
        }
    ]
}
```

#### Start Model Server Container with Downloaded Model
Start the container with the image pulled in the previous step and mount `<models_dir>` :
```Bash
docker run --rm -d -v <models_dir>:/models -p 9000:9000 openvino/model_server:latest --config_path /models/config.json --port 9000
```

#### Run the Client
```Bash
cd ../example_client
virtualenv .venv
. .venv/bin/activate
pip install -r client_requirements.txt
mkdir results_500x500 results_600x400

python face_detection.py --width 500 --height 500 --input_images_dir images/people --output_dir results_500x500

python face_detection.py --width 600 --height 400 --input_images_dir images/people --output_dir results_600x400
```
Results of running the client will be available in directories specified in `--output_dir`