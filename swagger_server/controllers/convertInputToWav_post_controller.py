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

def language_sloth_rest_convertInputToWav_post(file=None, input_language=None, target_language=None):  # noqa: E501
    """language_sloth_rest_convert_input_to_wav_post

    Converts input audio to WAV and send it to TTS and STT

    :param file: 
    :type file: strstr
    :param input_language: 
    :type input_language: str
    :param target_language: 
    :type target_language: str

    :rtype: str
    """

    if 'file' not in request.files:
        return {"status": "No file included!"}, 409

    file = request.files['file']

    if file.filename == '':
        return {"status": "No file selected!"}, 404

    #192.168.0.227
    stt_url = 'http://languagesloth_stt:5000/speech_to_text'
    data = {'lang': 'de'}

    if file:
        with open(os.path.join(UPLOAD_FOLDER, "recording.wav"), "wb") as fp:
            fp.write(file.read())
        
        with open(os.path.join(UPLOAD_FOLDER, "recording.wav"), "rb") as f:
            r = requests.post(stt_url, files={'file': f}, data=data)
            print(r.text)
            return r.text
        
            
        
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