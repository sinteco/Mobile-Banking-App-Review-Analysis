
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

### Files
- `scrape_reviews.py`: Script to scrape reviews from Google Play.
- `clean_reviews.py`: Script to preprocess and clean the review data.
- `data/raw_reviews.csv`: Raw scraped reviews.
- `data/clean_reviews.csv`: Cleaned review data ready for analysis.
