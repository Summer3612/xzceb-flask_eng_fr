import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from ibm_watson import ApiException

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



def englishToFrench(englishText):
   
    frenchText = language_translator.translate(
        text = englishText,
        model_id = 'en-es').get_result()
    
    return frenchText


if __name__ =='__main__':
    print (englishToFrench('hello'))

    