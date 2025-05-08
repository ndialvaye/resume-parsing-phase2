import re
import os
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from PyPDF2 import PdfReader

nltk.download("wordnet")

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def clean_text(text):
    lemmatizer = WordNetLemmatizer()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    tokens = text.lower().split()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

def save_to_excel(filename, cleaned_text):
    df = pd.DataFrame([{"Fichier": filename, "Texte_Nettoyé": cleaned_text}])
    output_path = "cleaned_data.xlsx"
    if os.path.exists(output_path):
        df_existing = pd.read_excel(output_path)
        df = pd.concat([df_existing, df], ignore_index=True)
    df.to_excel(output_path, index=False)
