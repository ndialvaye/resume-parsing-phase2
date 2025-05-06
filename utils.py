import fitz  # PyMuPDF
import re
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Assure le téléchargement dans Streamlit Cloud
nltk.download("punkt")
nltk.download("wordnet")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(t.lower()) for t in tokens]
    return " ".join(lemmatized)

def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("result_cleaned_phase2.xlsx", index=False)
