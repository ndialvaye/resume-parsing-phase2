import streamlit as st
from utils import extract_text_from_pdf, clean_text
import os
import pandas as pd

st.set_page_config(page_title="Phase 2 - Nettoyage des CVs", layout="wide")
st.title("🧹 Phase 2 - Extraction et Nettoyage Automatisé de CVs")

uploaded_files = st.file_uploader("Chargez un ou plusieurs fichiers PDF", type="pdf", accept_multiple_files=True)

if uploaded_files:
    data = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        cleaned = clean_text(text)
        data.append({"Nom du fichier": file.name, "Texte nettoyé": cleaned})

    df = pd.DataFrame(data)
    output_file = "phase2_clean_nltk/cv_cleaned.xlsx"
    os.makedirs("phase2_clean_nltk", exist_ok=True)
    df.to_excel(output_file, index=False)
    st.success("Fichier généré avec succès !")
    st.download_button("📥 Télécharger le fichier Excel", data=open(output_file, "rb"), file_name="cv_cleaned.xlsx")