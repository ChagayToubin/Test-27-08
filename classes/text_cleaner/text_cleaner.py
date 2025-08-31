import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")


class TextCleaner:


    @staticmethod
    def clean_text(text : str) -> str:
        text = TextCleaner.remove_marks(text)
        text = TextCleaner.remove_unnecessary_spaces(text)
        text = TextCleaner.lower_text(text)
        text = text.split()
        text = TextCleaner.remove_stopwords(text)
        text = TextCleaner.stemming(text)
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