
from textblob import TextBlob

class SentimentAnalysis:
    @staticmethod
    def sentiment_analyzer(text):
        blob = TextBlob(text)
        score = blob.sentiment.polarity

        if score < -0.2:
            return 'Negative'
        elif score > 0.2:
            return 'Positive'
        else:
            return 'Neutral'
        

