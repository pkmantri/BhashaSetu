import streamlit as st
from db import create_tables
from auth.auth import signup_user, login_user

st.set_page_config(page_title="BhashaSetu Pro", layout="wide")

create_tables()

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in:
    st.title("🔐 Login to BhashaSetu Pro")
    st.caption("Your personalized language learning dashboard")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Create Account"):
            if signup_user(new_user, new_pass):
                st.success("Account created! You can login now.")
            else:
                st.error("Username already exists")

    st.stop()

# ---------- DASHBOARD ----------
st.sidebar.title("🌐 BhashaSetu Pro")
st.sidebar.success(f"Logged in as {st.session_state.username}")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "✍ Text Analyzer",
        "🎙 Voice Translator",
        "📊 Progress",
        "💬 Conversation",
        "⚙ Logout"
    ]
)

if page == "🏠 Dashboard":
    st.header("🏠 Dashboard")
    st.info("Welcome! Select a feature from the sidebar.")

elif page == "✍ Text Analyzer":
    from features.text_analyzer import analyze_text, translate_text
    from db import update_progress

    st.header("✍ Text Analyzer")
    st.caption("Check grammar, correct mistakes, and translate text")

    text = st.text_area(
        "Enter your text",
        height=150,
        placeholder="Example: I am go to school yesterday"
    )

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Odia": "or",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te"
    }

    target_lang_name = st.selectbox(
        "Translate corrected text to",
        list(languages.keys())
    )

    if st.button("Analyze Text"):
        if not text.strip():
            st.warning("Please enter some text")
        else:
            # ✅ SAFE: variables defined before use
            target_lang_code = languages[target_lang_name]

            errors, corrected = analyze_text(text)

            st.subheader("✅ Corrected Text")
            st.success(corrected)

            if errors:
                st.subheader("❌ Detected Errors")
                for i, err in enumerate(errors, 1):
                    st.markdown(f"**{i}. {err['message']}**")
                    st.markdown(f"- Context: `{err['error']}`")
                    if err["suggestions"]:
                        st.markdown(
                            f"- Suggestions: {', '.join(err['suggestions'][:3])}"
                        )
            else:
                st.info("No grammar issues detected 🎉")

            translated = translate_text(corrected, target_lang_code)

            st.subheader("🌍 Translated Text")
            st.info(translated)

            # ✅ Progress update (NO NameError possible)
            update_progress(
                st.session_state.username,
                target_lang_name
            )

elif page == "🎙 Voice Translator":
    import os
    import numpy as np
    import scipy.io.wavfile as wav
    from audiorecorder import audiorecorder

    from modules.speech_to_text import speech_to_text
    from modules.translator import translate_text
    from modules.text_to_speech import text_to_speech

    st.header("🎙 Voice Translator")
    st.caption("Speak → Convert to text → Translate")

    audio = audiorecorder("🎤 Start Recording", "⏹ Stop Recording")

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Odia": "or",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te"
    }

    target_lang_name = st.selectbox(
        "Translate to",
        list(languages.keys())
    )
    target_lang_code = languages[target_lang_name]

    if len(audio) > 0:
        if not os.path.exists("audio"):
            os.makedirs("audio")

        audio_path = "audio/input.wav"

        samples = np.array(audio.get_array_of_samples())
        wav.write(audio_path, audio.frame_rate, samples)

        st.audio(audio_path)

        with st.spinner("🧠 Converting speech to text..."):
            text = speech_to_text(audio_path)

        st.subheader("📝 Recognized Text")
        st.success(text)

        with st.spinner("🌍 Translating..."):
            translated = translate_text(text, target_lang_code)

        st.subheader("🌍 Translated Text")
        st.info(translated)

        # OPTIONAL: speak translated text
        if st.button("🔊 Speak Translation"):
            output_audio = text_to_speech(
                translated,
                target_lang_code,
                "audio/output.mp3"
            )
            st.audio(output_audio)


elif page == "📊 Progress":
    import pandas as pd
    import matplotlib.pyplot as plt
    from db import get_progress

    st.header("📊 Language Learning Progress")
    st.caption("Track how many times you practiced each language")

    data = get_progress(st.session_state.username)

    if not data:
        st.info("No learning data yet. Start using Text Analyzer!")
    else:
        df = pd.DataFrame(data, columns=["Language", "Count"])

        st.subheader("📈 Practice Count per Language")
        st.bar_chart(df.set_index("Language"))

        st.subheader("🥧 Language Distribution")
        fig, ax = plt.subplots()
        ax.pie(
            df["Count"],
            labels=df["Language"],
            autopct="%1.1f%%",
            startangle=90
        )
        ax.axis("equal")
        st.pyplot(fig)

        st.subheader("📋 Detailed Table")
        st.dataframe(df)


elif page == "💬 Conversation":
    from features.conversation import process_message

    st.header("💬 Conversation Mode")
    st.caption("Practice languages by chatting with corrections and translations")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Odia": "or",
        "Bengali": "bn",
        "Tamil": "ta",
        "Telugu": "te"
    }

    target_lang_name = st.selectbox(
        "Translate replies to",
        list(languages.keys())
    )
    target_lang_code = languages[target_lang_name]

    user_message = st.text_input(
        "Type your message",
        placeholder="Example: I am learning English"
    )

    if st.button("Send"):
        if not user_message.strip():
            st.warning("Please type a message")
        else:
            result = process_message(user_message, target_lang_code)

            st.session_state.chat_history.append(result)

    # Display conversation
    if st.session_state.chat_history:
        st.subheader("🗨 Conversation")
        for msg in st.session_state.chat_history[::-1]:
            st.markdown("**🧑 You:**")
            st.write(msg["original"])

            st.markdown("**✅ Corrected:**")
            st.success(msg["corrected"])

            st.markdown("**🌍 Translated:**")
            st.info(msg["translated"])

            st.markdown("**🧠 Explain Simply:**")
            st.caption(msg["explanation"])

            st.divider()

    if st.button("🗑 Clear Conversation"):
        st.session_state.chat_history = []
        st.success("Conversation cleared")


elif page == "⚙ Logout":
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()
