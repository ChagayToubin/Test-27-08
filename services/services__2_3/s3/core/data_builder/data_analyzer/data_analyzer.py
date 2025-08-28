import nltk
from dateutil import parser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

class DataAnalyzer:


    @staticmethod
    def find_words_in_blacklist(words : list[str], blacklist : set[str]) -> set[str]:
        words_in_blacklist = {''}
        for word in words:
            if word in blacklist:
                words_in_blacklist.add(word)
        return words_in_blacklist



    @staticmethod
    def classify_sentiment(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score['compound'] >= 0.5:
            return "Positive"
        elif score['compound'] <= -0.5:
            return "Negative"
        else:
            return "Neutral"


    @staticmethod
    def get_dates_in_text(words : list):
        dates = []
        for word in words:
            try:
                date = parser.parse(word, dayfirst=True)
                dates.append(date)
            except (ValueError, OverflowError):
                pass
        if dates:
            return max(dates).strftime("%Y-%m-%d")





