import os

import connexion
import six
import requests
import json
import flask

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from swagger_server import util
from pydub import AudioSegment
from io import BytesIO
import base64

from flask import Flask, request

UPLOAD_FOLDER = './files'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def language_sloth_rest_convertInputToWav_post(file=None):  # noqa: E501
    """language_sloth_rest_convertInputToWav_post

    Retrieves the translation for a given text # noqa: E501

    :rtype: str
    """
    
    print(app)


    if 'file' not in request.files:
        return {"status": "No file part"}, 409

    file = request.files['file']

    if file.filename == '':
        return {"status": "No selected file"}, 404

    if file:
        #filename = secure_filename(file.filename)

        with open(os.path.join(UPLOAD_FOLDER, "test.webm"), "wb") as fp:
            fp.write(file.read())
        


        #filename = secure_filename(file.filename)

        #file.open("test.webm", "wb")
        #ad()
        
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'blob.wav'))

        # with open("file.webm", "wb") as f:
        #     file_stream = file.read()
        #     print(f)
        #     file.write(file_stream)
        #     print(f)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], f.name))
        
        
        #filename = secure_filename(file.filename)



        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return ('hello')
    
    
    #print(file)
    #fileRead = file.read()
    #print(fileRead)

    #f = open('test.wav', 'wb')
    #f.write(fileRead)
    #f.close()


    #print(f)
    #print(fileRead.size)
    #print(fileRead.type)

    #given_audio = AudioSegment.from_file(f, format="webm")

    #Call the translation   
    return 'request.form'