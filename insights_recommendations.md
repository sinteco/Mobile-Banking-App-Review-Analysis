# Insights and Recommendations

## Summary by Bank

### Commercial Bank of Ethiopia (CBE)
- **Driver:** Strong positive sentiment around app reliability and UI/UX (DistilBERT positive ratio >80%; themes emphasize UI/UX and general satisfaction).
- **Pain Point:** Support for overseas customers and verification flows generate negative reviews (verification key complaints for users abroad).
- **Recommended Improvements:**
  1. Introduce remote verification and in-app customer support for diaspora users.
  2. Enhance tutorials/FAQs covering security and account recovery, specifically for travel scenarios.

### Bank of Abyssinia (BOA)
- **Driver:** Positive feedback on app functionality (general satisfaction keyword cluster) and mobile convenience.
- **Pain Point:** Performance complaints (slow loading, app not working) dominate negative reviews.
- **Recommended Improvements:**
  1. Prioritize app performance optimization (startup time, transaction latency).
  2. Launch proactive push notifications or status dashboards to inform users when services are degraded.

### Dashen Bank
- **Driver:** High satisfaction with features (word cloud highlights "super", "wow", "dashen"). Positive scores across rating buckets.
- **Pain Point:** Login/access errors for a small but vocal minority (themes mention UI/UX with friction, negative rating clusters focus on login).
- **Recommended Improvements:**
  1. Improve resiliency of authentication flows (offline token caching, clearer error handling).
  2. Expand personalization features (budgeting tips, premium dashboard) to leverage already positive sentiment.

## Cross-Bank Comparisons
- CBE and Dashen enjoy stronger positive sentiment in 4-5 star ranges (mean >0.96). BOA shows lower VADER/TB scores at lower ratings, confirming performance friction.
- All banks share UI/UX as a major theme; however, only BOA has "Performance" mapped, indicating a specific bottleneck.

## Ethical Considerations
- Reviews show negative skew on BOA due to performance outages; manual sampling suggests potential duplicates or campaign-driven bursts (mitigated during preprocessing but noted as bias).
- International customers highlight location-based friction, indicating sample bias toward urban/diaspora segments.

## Supporting Evidence
- See `data/sentiment_agg.csv` for detailed mean scores by bank and rating.
- Keyword and theme files (`data/bank_keywords.csv`, `data/bank_themes.csv`) provide the thematic grouping logic referenced above.
