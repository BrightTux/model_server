# Dynamic Shape with Automatic Model Reloading{#ovms_docs_dynamic_shape_auto_reload}

## Introduction
This guide explains how to configure a model to accept input data in different shapes. In this example, it is done by reloading the model with a new shape each time it receives the request with a shape different than the one which is currently set. 

Enable dynamic shape via model reloading by setting the `shape` parameter to `auto`. To configure and use the dynamic batch size, take advantage of:

- Example client in Python [face_detection.py](https://github.com/openvinotoolkit/model_server/blob/v2021.4.2/example_client/face_detection.py) that can be used to request inference with the desired input shape.

- An example [face_detection_retail_0004](https://docs.openvinotoolkit.org/2021.4/omz_models_model_face_detection_retail_0004.html) model.

When using the `face_detection_retail_0004` model with the `face_detection.py` script, images are reloaded and resized to the desired width and height. Then, the output is processed from the server, and the inference results are displayed with bounding boxes drawn around the predicted faces. 

## Steps
Clone OpenVINO&trade; Model Server GitHub repository and enter `model_server` directory.
```
git clone https://github.com/openvinotoolkit/model_server.git
cd model_server
```
#### Download the Pretrained Model
Download the model files and store them in the `models` directory
```Bash
mkdir -p models/face_detection/1
curl https://storage.openvinotoolkit.org/repositories/open_model_zoo/2021.4/models_bin/3/face-detection-retail-0004/FP32/face-detection-retail-0004.bin https://storage.openvinotoolkit.org/repositories/open_model_zoo/2021.4/models_bin/3/face-detection-retail-0004/FP32/face-detection-retail-0004.xml -o models/face_detection/1/face-detection-retail-0004.bin -o models/face_detection/1/face-detection-retail-0004.xml
```

#### Pull the Latest Model Server Image
Pull the latest version of OpenVINO&trade; Model Server from Docker Hub:
```Bash
docker pull openvino/model_server:latest
```

#### Start the Model Server Container with the Model and Dynamic Batch Size
Start the container using the image pulled in the previous step and mount the `models` directory:
```Bash
docker run --rm -d -v $(pwd)/models:/models -p 9000:9000 openvino/model_server:latest --model_name face_detection --model_path /models/face_detection --shape auto --port 9000
```

#### Run the Client
```Bash
cd example_client
virtualenv .venv
. .venv/bin/activate
pip install -r client_requirements.txt
mkdir results_500x500 results_600x400

python face_detection.py --width 500 --height 500 --input_images_dir images/people --output_dir results_500x500

python face_detection.py --width 600 --height 400 --input_images_dir images/people --output_dir results_600x400
```
The results from running the client will be saved in the directory specified by `--output_dir`


>**NOTE**: reloading the model takes time and during each reload new requests are queued. Frequent model reloading may negatively affect overall performance. 