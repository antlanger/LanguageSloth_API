import connexion
import six
import requests
import json

from swagger_server import util


def language_sloth_rest_libretranslate_get(text):  # noqa: E501
    """language_sloth_rest_libretranslate_get

    Retrieves a file from the filesystem # noqa: E501

    :param text: text to translate
    :type text: str

    :rtype: str
    """

    #Call the translation
    url = 'http://192.168.0.228:5000/translate'
    params = {'q': text, 'source': 'en', 'target': 'es', 'format':'text'}

    jsonResponse =  requests.post(url=url, data=params)
    stringResponse = json.loads(jsonResponse.content)
    translatedText = stringResponse["translatedText"]

    print(translatedText)
    return translatedText
