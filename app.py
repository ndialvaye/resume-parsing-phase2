import streamlit as st
from utils import extract_text_from_pdf, clean_text, save_to_excel
import os
import tempfile

st.set_page_config(page_title="Resume Parsing - Phase 2", layout="centered")
st.title("📄 Resume Cleaner (Phase 2 - GOMYCODE)")

uploaded_files = st.file_uploader("Upload CVs (PDF uniquement)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    all_results = []
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        raw_text = extract_text_from_pdf(tmp_path)
        cleaned_text = clean_text(raw_text)

        all_results.append({"Nom du fichier": uploaded_file.name, "Texte Nettoyé": cleaned_text})

    save_to_excel(all_results)
    st.success("✅ Données nettoyées et sauvegardées dans 'result_cleaned_phase2.xlsx'")
    st.download_button("📥 Télécharger le fichier Excel", "result_cleaned_phase2.xlsx")
