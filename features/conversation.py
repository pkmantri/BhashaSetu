from features.text_analyzer import analyze_text, translate_text

def process_message(text, target_lang_code):
    errors, corrected = analyze_text(text)
    translated = translate_text(corrected, target_lang_code)

    # Simple rule-based explanation
    explanation = (
        "This sentence was corrected to improve grammar and clarity. "
        "The translation helps you understand it in another language."
    )

    return {
        "original": text,
        "corrected": corrected,
        "translated": translated,
        "explanation": explanation
    }
