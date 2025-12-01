-- PostgreSQL schema for bank_reviews project

CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) NOT NULL,
    app_name VARCHAR(255) NOT NULL
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INTEGER REFERENCES banks(bank_id),
    review_text TEXT NOT NULL,
    rating INTEGER,
    review_date DATE,
    sentiment_label VARCHAR(32),
    sentiment_score FLOAT,
    source VARCHAR(64)
);
