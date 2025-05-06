
import streamlit as st
import os
import fitz  # PyMuPDF
import docx2txt
from utils import clean_text, extract_text_from_pdf, extract_text_from_docx
import pandas as pd

# Configuration
st.set_page_config(page_title="Nettoyage CV - Phase 2", layout="wide")

st.title("Phase 2 - Extraction et Nettoyage Automatique des CVs")

uploaded_files = st.file_uploader(
    "Déposez les CV ici (PDF ou Word)", 
    type=["pdf", "docx"], 
    accept_multiple_files=True
)

results = []

if uploaded_files:
    for file in uploaded_files:
        filename = file.name
        file_extension = os.path.splitext(filename)[1].lower()

        # Sauvegarde temporaire
        os.makedirs("uploads", exist_ok=True)
        os.makedirs("results", exist_ok=True)
        file_path = os.path.join("uploads", filename)
        with open(file_path, "wb") as f:
            f.write(file.read())

        # Extraction de texte
        if file_extension == ".pdf":
            raw_text = extract_text_from_pdf(file_path)
        elif file_extension == ".docx":
            raw_text = extract_text_from_docx(file_path)
        else:
            st.error("Format non supporté.")
            continue

        cleaned_text = clean_text(raw_text)
        results.append({
            "Nom du fichier": filename,
            "Texte nettoyé": cleaned_text
        })

    df = pd.DataFrame(results)
    output_path = os.path.join("results", "cv_nettoyes_phase2.xlsx")
    df.to_excel(output_path, index=False)
    st.success("Extraction terminée. Fichier généré :")
    st.download_button("📥 Télécharger le fichier Excel", data=open(output_path, "rb"), file_name="cv_nettoyes_phase2.xlsx")

