import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'bank_reviews',
    'user': 'postgres',
    'password': 'yourpassword',
}

BANKS = [
    {"bank_name": "Commercial Bank of Ethiopia", "app_name": "com.combanketh.mobilebanking"},
    {"bank_name": "Bank of Abyssinia", "app_name": "com.boa.boaMobileBanking"},
    {"bank_name": "Dashen Bank", "app_name": "com.dashen.dashensuperapp"}
]

def insert_banks(cur):
    cur.execute("DELETE FROM banks;")
    for bank in BANKS:
        cur.execute(
            "INSERT INTO banks (bank_name, app_name) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
            (bank["bank_name"], bank["app_name"])
        )

def get_bank_id(cur, bank_name):
    cur.execute("SELECT bank_id FROM banks WHERE bank_name = %s;", (bank_name,))
    return cur.fetchone()[0]

def insert_reviews(cur, reviews_df):
    reviews = []
    for _, row in reviews_df.iterrows():
        bank_id = get_bank_id(cur, row['bank'])
        reviews.append((
            bank_id,
            row['review'],
            int(row['rating']) if not pd.isnull(row['rating']) else None,
            row['date'],
            row['distilbert_label'],
            float(row['distilbert_score']) if not pd.isnull(row['distilbert_score']) else None,
            row['source']
        ))
    execute_values(cur, """
        INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
        VALUES %s
    """, reviews)

def main():
    df = pd.read_csv('data/sentiment_reviews.csv')
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    insert_banks(cur)
    conn.commit()
    insert_reviews(cur, df)
    conn.commit()
    cur.close()
    conn.close()
    print("Inserted reviews into PostgreSQL.")

if __name__ == "__main__":
    main()
