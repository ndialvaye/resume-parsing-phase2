import streamlit as st
import os
from utils import extract_text_from_pdf, clean_text, save_to_excel

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Phase 2 - Extraction et Nettoyage des CVs")

uploaded_files = st.file_uploader("Uploader un ou plusieurs fichiers PDF", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    results = []
    for uploaded_file in uploaded_files:
        filepath = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())

        raw_text = extract_text_from_pdf(filepath)
        cleaned_text = clean_text(raw_text)
        results.append({"filename": uploaded_file.name, "cleaned_text": cleaned_text})

    if results:
        save_to_excel(results)
        st.success("Traitement terminé. Résultats sauvegardés dans le fichier `cleaned_cvs.xlsx`.")
        st.download_button("📥 Télécharger le fichier Excel", data=open("cleaned_cvs.xlsx", "rb"), file_name="cleaned_cvs.xlsx")