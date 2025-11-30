import pandas as pd
from google_play_scraper import reviews, Sort
import time

BANK_APPS = [
    {"name": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking"},
    {"name": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking"},
    {"name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp"}
]

REVIEWS_PER_BANK = 400

all_reviews = []

for bank in BANK_APPS:
    print(f"Scraping reviews for {bank['name']}...")
    count = 0
    next_token = None
    while count < REVIEWS_PER_BANK:
        batch, next_token = reviews(
            bank["app_id"],
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=min(200, REVIEWS_PER_BANK - count),
            continuation_token=next_token
        )
        for r in batch:
            all_reviews.append({
                "review": r["content"],
                "rating": r["score"],
                "date": r["at"].strftime("%Y-%m-%d"),
                "bank": bank["name"],
                "source": "Google Play"
            })
        count += len(batch)
        if not next_token or len(batch) == 0:
            break
        time.sleep(1)

print(f"Total reviews scraped: {len(all_reviews)}")

df = pd.DataFrame(all_reviews)
df.to_csv("data/raw_reviews.csv", index=False)
print("Saved to data/raw_reviews.csv")
