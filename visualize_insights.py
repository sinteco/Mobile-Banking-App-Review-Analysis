import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv('data/sentiment_reviews.csv')
keywords = pd.read_csv('data/bank_keywords.csv')

# Sentiment bar plot by bank
def plot_sentiment_bar(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='bank', hue='distilbert_label', order=df['bank'].value_counts().index)
    plt.title('Sentiment Distribution by Bank (DistilBERT)')
    plt.xlabel('Bank')
    plt.ylabel('Review Count')
    plt.legend(title='Sentiment')
    plt.tight_layout()
    plt.savefig('plots/sentiment_bar.png')
    plt.close()

# Keyword frequency bar plot
def plot_keyword_bar(keywords):
    plt.figure(figsize=(10, 5))
    top_keywords = keywords.groupby(['bank', 'keyword']).size().reset_index(name='count')
    for bank in keywords['bank'].unique():
        bank_kw = top_keywords[top_keywords['bank'] == bank].nlargest(10, 'count')
        plt.bar(bank_kw['keyword'], bank_kw['count'], label=bank)
    plt.title('Top Keywords per Bank')
    plt.xlabel('Keyword')
    plt.ylabel('Frequency')
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('plots/keyword_bar.png')
    plt.close()

# Word cloud for each bank
def plot_wordclouds(keywords):
    for bank in keywords['bank'].unique():
        text = ' '.join(keywords[keywords['bank'] == bank]['keyword'])
        wc = WordCloud(width=800, height=400, background_color='white').generate(text)
        plt.figure(figsize=(8, 4))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud for {bank}')
        plt.tight_layout()
        plt.savefig(f'plots/wordcloud_{bank.replace(" ", "_").lower()}.png')
        plt.close()

if __name__ == "__main__":
    import os
    os.makedirs('plots', exist_ok=True)
    plot_sentiment_bar(df)
    plot_keyword_bar(keywords)
    plot_wordclouds(keywords)
    print('Plots saved in the plots/ directory.')
