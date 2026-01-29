import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Chatbot Gemini", page_icon="🤖")

# Titre
st.title("🤖 Chatbot Gemini")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Clé API manquante ! Créez un fichier .env avec GEMINI_API_KEY=votre_clé")
    st.stop()

genai.configure(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Votre message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
