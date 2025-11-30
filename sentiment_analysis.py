
import pandas as pd
from transformers import pipeline
from tqdm import tqdm
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import numpy as np

def distilbert_sentiment(text, analyzer):
    try:
        result = analyzer(str(text))[0]
        label = result['label']
        score = result['score']
    except Exception:
        label = 'NEUTRAL'
        score = 0.5
    return label, score

def vader_sentiment(text, analyzer):
    try:
        vs = analyzer.polarity_scores(str(text))
        compound = vs['compound']
        if compound >= 0.05:
            label = 'POSITIVE'
        elif compound <= -0.05:
            label = 'NEGATIVE'
        else:
            label = 'NEUTRAL'
        score = compound
    except Exception:
        label = 'NEUTRAL'
        score = 0.0
    return label, score

def textblob_sentiment(text):
    try:
        tb = TextBlob(str(text))
        polarity = tb.sentiment.polarity
        if polarity > 0.1:
            label = 'POSITIVE'
        elif polarity < -0.1:
            label = 'NEGATIVE'
        else:
            label = 'NEUTRAL'
        score = polarity
    except Exception:
        label = 'NEUTRAL'
        score = 0.0
    return label, score

def analyze_sentiment(input_csv, output_csv, agg_csv):
    df = pd.read_csv(input_csv)
    distilbert = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    vader = SentimentIntensityAnalyzer()

    distilbert_labels, distilbert_scores = [], []
    vader_labels, vader_scores = [], []
    textblob_labels, textblob_scores = [], []

    for review in tqdm(df['review'], desc="Analyzing sentiment"):
        # DistilBERT
        label, score = distilbert_sentiment(review, distilbert)
        distilbert_labels.append(label)
        distilbert_scores.append(score)
        # VADER
        v_label, v_score = vader_sentiment(review, vader)
        vader_labels.append(v_label)
        vader_scores.append(v_score)
        # TextBlob
        t_label, t_score = textblob_sentiment(review)
        textblob_labels.append(t_label)
        textblob_scores.append(t_score)

    df['distilbert_label'] = distilbert_labels
    df['distilbert_score'] = distilbert_scores
    df['vader_label'] = vader_labels
    df['vader_score'] = vader_scores
    df['textblob_label'] = textblob_labels
    df['textblob_score'] = textblob_scores

    df.to_csv(output_csv, index=False)
    print(f"Sentiment analysis complete. Results saved to {output_csv}")

    # Aggregation by bank and rating
    agg = df.groupby(['bank', 'rating']).agg(
        distilbert_mean_score = ('distilbert_score', 'mean'),
        vader_mean_score = ('vader_score', 'mean'),
        textblob_mean_score = ('textblob_score', 'mean'),
        count = ('review', 'count')
    ).reset_index()
    agg.to_csv(agg_csv, index=False)
    print(f"Aggregated sentiment by bank and rating saved to {agg_csv}")

if __name__ == "__main__":
    analyze_sentiment("data/clean_reviews.csv", "data/sentiment_reviews.csv", "data/sentiment_agg.csv")
