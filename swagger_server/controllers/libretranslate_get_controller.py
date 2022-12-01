import connexion
import six
import requests
import json

from swagger_server import util


def language_sloth_rest_libretranslate_get(text, source_language, target_language):  # noqa: E501
    """language_sloth_rest_libretranslate_get

    Retrieves the translation for a given text # noqa: E501

    :param text: text to translate
    :type text: str
    :param source_language: source language of the text
    :type source_language: str
    :param target_language: target language of the text
    :type target_language: str

    :rtype: str
    """

    #Call the translation
    url = 'http://192.168.0.228:5000/translate'
    params = {'q': text, 'source': source_language, 'target': target_language, 'format':'text'}

    jsonResponse =  requests.post(url=url, data=params)
    stringResponse = json.loads(jsonResponse.content)
    translatedText = stringResponse["translatedText"]

    print(translatedText)
    return translatedText
