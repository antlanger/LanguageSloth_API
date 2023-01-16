import os

import connexion
import six
import requests
import json
import flask
from pydub import AudioSegment

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
    input_lang = request.form['inputLanguage']
    output_lang = request.form['targetLanguage']
    print(input_lang, flush=True)

    if file.filename == '':
        return {"status": "No file selected!"}, 404

    stt_url = 'http://languagesloth_tts:5001/speech_to_text'
    tts_url = 'http://languagesloth_tts:5001/text_to_speech'
    libre_url = 'http://languagesloth_libretranslate:5000/translate'

    webm_path = os.path.join(UPLOAD_FOLDER, "recording.webm")
    wav_path = os.path.join(UPLOAD_FOLDER, "recording.wav")

    if file:
        with open(webm_path, "wb") as fp:
            fp.write(file.read())
        
        with open(webm_path, "rb") as f:
            data = {'lang': input_lang}
            response_stt = requests.post(stt_url, files={'file': f}, data=data)
            print(f"TEXT: {response_stt.text}", flush=True)
        

        # TODO Send received text to LibreTranslate
        params = {'q': response_stt.text, 'source': input_lang, 'target': output_lang, 'format':'text'}

        jsonResponse =  requests.post(url=libre_url, data=params)
        stringResponse = json.loads(jsonResponse.content)
        translatedText = stringResponse["translatedText"]

        print(f"Translated text: {translatedText}", flush=True)

        data = {'lang': output_lang, 'text': translatedText} #TODO change to output_lang when libretranslate works
        response_tts = requests.post(tts_url, data=data)
        response_file = response_tts.content

        with open(wav_path, "wb") as fp:
            fp.write(response_file)

        AudioSegment.from_file(wav_path).export(webm_path, format="webm")
        
        webm_path = "/usr/src/app/files/recording.webm"
        return send_file(
         webm_path, 
         mimetype="audio/webm", 
         as_attachment=True, 
         attachment_filename="translatedRecording.webm")

    return ('No file found!')