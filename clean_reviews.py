import pandas as pd

def clean_reviews(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    # Remove duplicates based on review text, rating, date, and bank
    df = df.drop_duplicates(subset=["review", "rating", "date", "bank"])
    # Drop rows with missing review or rating
    df = df.dropna(subset=["review", "rating"])
    # Normalize date format
    df["date"] = pd.to_datetime(df["date"], errors='coerce').dt.strftime('%Y-%m-%d')
    # Drop rows with invalid dates
    df = df.dropna(subset=["date"])
    # Reorder columns
    df = df[["review", "rating", "date", "bank", "source"]]
    df.to_csv(output_csv, index=False)
    print(f"Cleaned data saved to {output_csv}. Total rows: {len(df)}")

if __name__ == "__main__":
    clean_reviews("data/raw_reviews.csv", "data/clean_reviews.csv")
