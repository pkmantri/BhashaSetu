# 🌐 BhashaSetu 
**An AI-Powered Multilingual Learning & Translation Platform**

---

## 📌 Overview

**BhashaSetu** is a full-stack, AI-enabled language learning and translation web application built using **Python and Streamlit**.  
It helps users **learn, correct, translate, and practice multiple languages** through **text, conversation, and voice interaction**, while also tracking their learning progress visually.

The project focuses on **accessibility, simplicity, and real-world usability**, especially for students and multilingual users.

---

## ✨ Key Features

### 🔐 Authentication
- Custom Login & Signup system  
- Secure password hashing using `bcrypt`  
- User data stored locally using SQLite  
- Session-based authentication  

### ✍ Text Analyzer
- Grammar and error detection  
- Corrected sentence generation  
- Multilingual translation  

### 💬 Conversation Mode
- Text-based chat for language practice  
- Grammar correction + translation  
- Simple explanations for learning  

### 🎙 Voice Translator
- Voice → Text  
- Voice → Text → Translation  
- Optional Text → Speech  

### 📊 Progress Tracker
- Tracks language usage  
- Bar chart & pie chart analytics  

### 🌍 Multilingual Support
- English, Hindi, Odia, Bengali, Tamil, Telugu  
- Easily extendable to 30+ languages  

---

## 🧠 Tech Stack

- Frontend: Streamlit  
- Backend: Python  
- Database: SQLite  
- Grammar: language-tool-python  
- Translation: googletrans  
- Speech-to-Text: Whisper  
- Audio Input: streamlit-audiorecorder  

---

## 📁 Project Structure

```
BhashaSetu_Pro/
│
├── app.py
├── db.py
├── bhashasetu.db
│
├── auth/
│   └── auth.py
│
├── features/
│   ├── text_analyzer.py
│   └── conversation.py
│
├── modules/
│   ├── speech_to_text.py
│   ├── translator.py
│   └── text_to_speech.py
│
├── analytics/
├── audio/
├── assets/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

```bash
py -3.10 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎓 Use Cases

- Language learning  
- Grammar correction  
- Multilingual communication  
- Voice translation  

---

## 🚀 Future Scope

- 30+ languages  
- AI-based explanations  
- Voice conversation  
- Cloud deployment  

---

## 🧑‍💻 Author

**Pankaj Mantri**  
BSc Information Science & Telecommunication  
Ravenshaw University  

---

## 📜 License

Educational use only.
