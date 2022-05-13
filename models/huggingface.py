from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def predict_sentiment(sentence: str):
    return sentiment_model(sentence)
