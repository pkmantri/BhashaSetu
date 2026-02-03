from googletrans import Translator
from langdetect import detect

translator = Translator()

def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    return translated.text
