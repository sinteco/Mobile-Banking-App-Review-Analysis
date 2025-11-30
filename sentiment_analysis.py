import pandas as pd
from transformers import pipeline
from tqdm import tqdm

def analyze_sentiment(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    sentiments = []
    for review in tqdm(df['review'], desc="Analyzing sentiment"):
        try:
            result = sentiment_analyzer(str(review))[0]
            label = result['label']
            score = result['score']
        except Exception:
            label = 'NEUTRAL'
            score = 0.5
        sentiments.append((label, score))
    df['sentiment_label'] = [s[0] for s in sentiments]
    df['sentiment_score'] = [s[1] for s in sentiments]
    df.to_csv(output_csv, index=False)
    print(f"Sentiment analysis complete. Results saved to {output_csv}")

if __name__ == "__main__":
    analyze_sentiment("data/clean_reviews.csv", "data/sentiment_reviews.csv")
