import streamlit as st
from utils import extract_text_from_pdf, clean_text, save_to_excel

st.title("🧹 Nettoyage et structuration de CVs - Phase 2")

uploaded_files = st.file_uploader("📄 Uploadez vos CVs (PDF uniquement)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(text)
        st.text_area(f"🧾 Texte nettoyé - {uploaded_file.name}", cleaned_text, height=300)
        save_to_excel(uploaded_file.name, cleaned_text)
    st.success("✅ Tous les fichiers ont été traités et enregistrés.")
