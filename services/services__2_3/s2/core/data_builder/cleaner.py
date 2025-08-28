import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")


class Cleaner:


    @staticmethod
    def clean_text(text : str) -> str:
        text = Cleaner.remove_marks(text)
        text = Cleaner.remove_unnecessary_spaces(text)
        text = Cleaner.lower_text(text)
        text = text.split()
        text = Cleaner.remove_stopwords(text)
        text = Cleaner.stemming(text)
        return " ".join(text)


    @staticmethod
    def remove_marks(text : str) -> str:
        return re.sub(r"[^\w\s]", " ", text)


    @staticmethod
    def remove_unnecessary_spaces(text : str) -> str:
        return re.sub(r"\s+", " ", text).strip()


    @staticmethod
    def remove_stopwords(words : list) -> list:
        stop_words = set(stopwords.words("english"))
        return [w for w in words if w not in stop_words]


    @staticmethod
    def lower_text(text : str) -> str:
        return text.lower()


    @staticmethod
    def stemming(words : list) -> list:
        ps = PorterStemmer()
        return [ps.stem(w) for w in words]