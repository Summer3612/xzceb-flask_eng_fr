import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def englishToFrench(english_text:str):
    result = language_translator.translate(
        text = english_text,
        model_id = 'en-fr').get_result()

    french_text = result['translations'][0]['translation']

    return french_text

def frenchToEnglish(french_text:str):
    #write the code here
    result = language_translator.translate(
        text = french_text,
        model_id = 'fr-en').get_result()
    english_text = result['translations'][0]['translation']

    return english_text


if __name__ =='__main__':
    print(frenchToEnglish(''))
    