from watson_developer_cloud import LanguageTranslatorV3
import json

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='6N2fgkLzRaDtj7vM90uDNYiBZY8rxYRdfzXKvQ0vqio9',
    url='https://gateway-lon.watsonplatform.net/language-translator/api'
)

translation = language_translator.translate(
    text='Hello',
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))