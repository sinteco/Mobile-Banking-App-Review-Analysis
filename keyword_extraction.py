import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def extract_keywords(input_csv, output_csv, top_n=10):
    df = pd.read_csv(input_csv)
    # Simple preprocessing: lowercase, remove non-alphabetic
    df['clean_review'] = df['review'].astype(str).apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x.lower()))
    results = []
    for bank in df['bank'].unique():
        bank_df = df[df['bank'] == bank]
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_features=100)
        X = vectorizer.fit_transform(bank_df['clean_review'])
        feature_array = vectorizer.get_feature_names_out()
        tfidf_sorting = X.sum(axis=0).A1.argsort()[::-1]
        top_keywords = feature_array[tfidf_sorting][:top_n]
        for kw in top_keywords:
            results.append({'bank': bank, 'keyword': kw})
    keywords_df = pd.DataFrame(results)
    keywords_df.to_csv(output_csv, index=False)
    print(f"Keywords extracted and saved to {output_csv}")

if __name__ == "__main__":
    extract_keywords("data/sentiment_reviews.csv", "data/bank_keywords.csv", top_n=10)
