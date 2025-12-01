import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_text(text):
    try:
        text = str(text).lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = text.split()
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if w not in stop_words]
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(w) for w in tokens]
        return ' '.join(tokens)
    except Exception:
        return ''

def extract_keywords(input_csv, output_csv, top_n=10):
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    df = pd.read_csv(input_csv)
    df['clean_review'] = df['review'].apply(preprocess_text)
    results = []
    for bank in df['bank'].unique():
        bank_df = df[df['bank'] == bank]
        if bank_df['clean_review'].str.strip().eq('').all():
            continue
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2), max_features=100)
        try:
            X = vectorizer.fit_transform(bank_df['clean_review'])
            feature_array = vectorizer.get_feature_names_out()
            tfidf_sorting = X.sum(axis=0).A1.argsort()[::-1]
            top_keywords = feature_array[tfidf_sorting][:top_n]
            for kw in top_keywords:
                results.append({'bank': bank, 'keyword': kw})
        except Exception:
            continue
    keywords_df = pd.DataFrame(results)
    keywords_df.to_csv(output_csv, index=False)
    print(f"Keywords extracted and saved to {output_csv}")

if __name__ == "__main__":
    extract_keywords("data/sentiment_reviews.csv", "data/bank_keywords.csv", top_n=10)
