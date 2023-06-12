# Detect face and hand landmarks using Python, Mediapipe and OpenCV

A Flask web app to switch on live video feed using webcam and detecting face and hand landmarks in real time.

## How to start Flask app ?

### Start virtual env
From cloned directory go to ```python_env``` and run
```bash
source ./bin/activate
```

### Run app
```bash
python app.py
```

Once you start an app, you can paste address given by app in your browser and run
http://<address>:<port>/ to check if it's working fine -> prints ok
http://<address>:<port>/track to start live video feed and start detecting face and hand landmarks

## To deploy in Docker container

### Build Docker Image
```bash
docker  build  -t  <image_name>:<tag>  .
```

### Start docker container
```bash
docker  container  run  -d   -p  5000:5000   <image_name>:<tag>
```

You might need to enable your webcam access for Docker Container, add below flag while starting docker container to enable webcam access inside container.
```bash
--device=/dev/video0:/dev/video0
```
https://stackoverflow.com/questions/44852484/access-webcam-using-opencv-python-in-docker


## Feel free to clone and improve it further and raise ticket if required.