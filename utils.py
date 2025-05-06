
import re
import fitz
import docx2txt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words("french")]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)
