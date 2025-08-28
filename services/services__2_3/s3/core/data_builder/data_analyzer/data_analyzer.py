import nltk
from datetime import datetime
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

class DataAnalyzer:


    @staticmethod
    def find_words_in_blacklist(words : list[str], blacklist : set[str]) -> set[str]:
        words_in_blacklist = set()
        for word in words:
            if word in blacklist:
                words_in_blacklist.add(word)
        return words_in_blacklist



    @staticmethod
    def classify_sentiment(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score >= 0.5:
            return "Positive"
        elif score <= -0.5:
            return "Negative"
        else:
            return "Neutral"


    @staticmethod
    def get_dates_in_text(words : list):
        time_format = "%d-%m-%Y"
        list_date = set()
        matches = words
        for match in matches:
            try:
                datetime.strptime(match, time_format)
                list_date.add(match)
            except ValueError:
                pass
        if list_date:
            return max(list_date)







