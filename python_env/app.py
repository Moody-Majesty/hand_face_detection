
from flask import Flask, Response
from face_hand_detection import main

app = Flask(__name__)


@app.route('/')
def check():
    return 'OK'


@app.route('/track')
def video_focus():
    to_do = main()
    return 'live video feed is on' #Response(main(), mimetype='multipart/x-mixed-replace; boundary=frame')
    