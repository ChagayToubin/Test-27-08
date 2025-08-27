import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download("stopwords")

class Cleaner:

    @staticmethod
    def clean_text(text):
        pass

    @staticmethod
    def remove_marks(text : str):
        return re.sub(r"[^\w\s]", " ", text)

    @staticmethod
    def remove_unnecessary_spaces(text : str):
        return re.sub(r"\s+", " ", text).strip()

    @staticmethod
    def remove_stopwords(words : list):
        stop_words = set(stopwords.words("english"))
        return [w for w in words if w not in stop_words]

    @staticmethod
    def lower_text(text : str):
        return text.lower()

    @staticmethod
    def stemming(words : list):
        ps = PorterStemmer()
        return [ps.stem(w) for w in words]