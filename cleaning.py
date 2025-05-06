import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

def clean_and_normalize(text):
    lemmatizer = WordNetLemmatizer()
    text = re.sub(r'[\r\n]+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.lower()

    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words("english")]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return {"cleaned_text": " ".join(tokens)}