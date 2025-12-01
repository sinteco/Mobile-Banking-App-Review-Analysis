-- SQL Verification Queries for Bank Reviews Database

-- 1. Count total reviews per bank
SELECT b.bank_name, COUNT(r.review_id) as total_reviews
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
ORDER BY total_reviews DESC;

-- 2. Average rating per bank
SELECT b.bank_name, ROUND(AVG(r.rating), 2) as avg_rating
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name
ORDER BY avg_rating DESC;

-- 3. Sentiment distribution per bank
SELECT b.bank_name, r.sentiment_label, COUNT(*) as count
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
GROUP BY b.bank_name, r.sentiment_label
ORDER BY b.bank_name, count DESC;

-- 4. Check for potential duplicates (if any slipped through)
SELECT review_text, COUNT(*)
FROM reviews
GROUP BY review_text
HAVING COUNT(*) > 1;

-- 5. Sample recent negative reviews for analysis
SELECT b.bank_name, r.rating, r.review_text
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
WHERE r.rating = 1
ORDER BY r.review_date DESC
LIMIT 5;
