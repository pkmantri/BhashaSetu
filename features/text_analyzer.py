import language_tool_python
from googletrans import Translator

tool = language_tool_python.LanguageTool('en-US')
translator = Translator()

def analyze_text(text):
    matches = tool.check(text)

    errors = []
    corrected_text = text

    for match in matches:
        errors.append({
            "message": match.message,
            "error": match.context,
            "suggestions": match.replacements
        })

    corrected_text = tool.correct(text)

    return errors, corrected_text


def translate_text(text, target_lang):
    translated = translator.translate(text, dest=target_lang)
    return translated.text
