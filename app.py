import streamlit as st
from cleaning import clean_and_normalize
import os
import pandas as pd

st.title("Nettoyage et Normalisation des CVs")

uploaded_files = st.file_uploader("Uploader un ou plusieurs fichiers texte", type=["txt"], accept_multiple_files=True)

if uploaded_files:
    results = []
    for uploaded_file in uploaded_files:
        text = uploaded_file.read().decode("utf-8")
        cleaned_data = clean_and_normalize(text)
        results.append(cleaned_data)
    
    df = pd.DataFrame(results)
    st.write("Résultat :")
    st.dataframe(df)

    output_path = "cleaned_output.xlsx"
    df.to_excel(output_path, index=False)
    st.success(f"Fichier sauvegardé : {output_path}")