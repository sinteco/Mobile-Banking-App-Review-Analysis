
# Mobile Banking App Review Analysis

## Methodology

### Data Collection
- Used `google-play-scraper` to collect user reviews from the Google Play Store for three Ethiopian banks:
	- Commercial Bank of Ethiopia (com.combanketh.mobilebanking)
	- Bank of Abyssinia (com.boa.boaMobileBanking)
	- Dashen Bank (com.dashen.dashensuperapp)
- Collected at least 400 reviews per bank, including review text, rating, date, bank name, and source.
- Saved raw reviews to `data/raw_reviews.csv`.

### Preprocessing
- Removed duplicate reviews based on review text, rating, date, and bank.
- Dropped rows with missing review or rating.
- Normalized date format to YYYY-MM-DD.
- Saved cleaned data to `data/clean_reviews.csv`.


### Sentiment & Thematic Analysis
- Sentiment analysis performed using three methods: DistilBERT (transformers), VADER, and TextBlob for comparison and robustness.
- Aggregated mean sentiment scores by bank and rating (see `data/sentiment_agg.csv`).
- Keyword extraction uses TF-IDF with tokenization, stopword removal, and lemmatization (see `keyword_extraction.py`).
- Themes are grouped using a rule-based mapping of keywords to 3–5 business-relevant categories per bank (see `theme_grouping.py`).
- All scripts include error handling and modular functions for maintainability.

### Database Schema (PostgreSQL)

The project uses PostgreSQL (via Docker) to store cleaned and processed review data. The schema consists of two tables:

**banks**
- `bank_id` SERIAL PRIMARY KEY
- `bank_name` VARCHAR(255) NOT NULL
- `app_name` VARCHAR(255) NOT NULL

**reviews**
- `review_id` SERIAL PRIMARY KEY
- `bank_id` INTEGER REFERENCES banks(bank_id)
- `review_text` TEXT NOT NULL
- `rating` INTEGER
- `review_date` DATE
- `sentiment_label` VARCHAR(32)
- `sentiment_score` FLOAT
- `source` VARCHAR(64)

See `bank_reviews_schema.sql` and `docker-compose.yml` for setup. Use `create_schema_pg.py` to create tables and `insert_reviews_pg.py` to insert data from CSV.

### Files
- `scrape_reviews.py`: Scrape reviews from Google Play.
- `clean_reviews.py`: Preprocess and clean the review data.
- `sentiment_analysis.py`: Modular sentiment analysis (DistilBERT, VADER, TextBlob) and aggregation.
- `keyword_extraction.py`: Robust keyword extraction with NLP preprocessing.
- `theme_grouping.py`: Rule-based theme grouping from extracted keywords.
- `data/raw_reviews.csv`: Raw scraped reviews.
- `data/clean_reviews.csv`: Cleaned review data ready for analysis.
- `data/sentiment_reviews.csv`: Reviews with sentiment scores and labels.
- `data/sentiment_agg.csv`: Aggregated sentiment by bank and rating.
- `data/bank_keywords.csv`: Top keywords per bank.
- `data/bank_themes.csv`: Themes per bank.
