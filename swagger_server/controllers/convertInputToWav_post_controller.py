import os

import connexion
import six
import requests
import json
import flask

from swagger_server import util
from io import BytesIO

from flask import Flask, request, send_file, make_response

UPLOAD_FOLDER = './files'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def language_sloth_rest_convertInputToWav_post(file=None):  # noqa: E501
    """language_sloth_rest_convertInputToWav_post

    Retrieves input recording, translates it to given language and returns output recording.

    :rtype: str
    """

    if 'file' not in request.files:
        return {"status": "No file included!"}, 409

    file = request.files['file']

    if file.filename == '':
        return {"status": "No file selected!"}, 404

    if file:
        with open(os.path.join(UPLOAD_FOLDER, "recording.wav"), "wb") as fp:
            fp.write(file.read())
        
        # TODO Send WAV to CoquiSST
        # TODO Send received text to LibreTranslate
        # TODO Send translated text to CoquiTTS
        # TODO Return output audio to frontend
        path_test = "/usr/src/app/files/recording.wav"
        
        
        
        return send_file(
         path_test, 
         mimetype="audio/wav", 
         as_attachment=True, 
         attachment_filename="translatedRecording.wav")

    return ('No file found!')