from gtts import gTTS
import os

# Languages supported by gTTS
GTTS_SUPPORTED = [
    "en", "hi", "bn", "ta", "te"
]

def text_to_speech(text, lang, output_path="audio/output.mp3"):
    if not os.path.exists("audio"):
        os.makedirs("audio")

    # Fallback if language not supported
    if lang not in GTTS_SUPPORTED:
        lang = "en"   # fallback to English

    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)

    return output_path
