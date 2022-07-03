""" Main translator module for Hands-on Lab: Python Web Application Creation and Deployment """
# import json
import os
from pathlib import Path
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv(Path("/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/.env"))
apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(VERSION,authenticator)
language_translator.set_service_url(url)
language_translator.set_default_headers({'x-watson-learning-opt-out': "true"})

def english_to_french(english_text):
    """ English to French Watson translation API usage """
    try:
        translation = language_translator.translate(english_text, model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    except ApiException as ex:
        return ex.code

def french_to_english(french_text):
    """ French to English Watson translation API usage """
    try:
        translation = language_translator.translate(french_text, model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    except ApiException as ex:
        return ex.code
