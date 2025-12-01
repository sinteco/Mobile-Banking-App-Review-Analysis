import pandas as pd

THEME_MAP = {
    'UI/UX': ['ui', 'interface', 'design', 'nice', 'look', 'user friendly'],
    'Performance': ['fast', 'slow', 'loading', 'performance', 'crash', 'working', 'work'],
    'Account Access': ['login', 'access', 'verification', 'account', 'register'],
    'Transactions': ['transfer', 'send', 'receive', 'payment', 'transaction'],
    'General Satisfaction': ['good', 'best', 'excellent', 'like', 'wow', 'super', 'application', 'app', 'bank', 'boa', 'cbe', 'dashen', 'mobile', 'service']
}

def group_themes(keywords_csv, output_csv, theme_map=THEME_MAP):
    try:
        df = pd.read_csv(keywords_csv)
    except Exception as e:
        print(f"Error reading {keywords_csv}: {e}")
        return
    results = []
    for bank in df['bank'].unique():
        bank_keywords = df[df['bank'] == bank]['keyword'].tolist()
        themes = set()
        for kw in bank_keywords:
            for theme, words in theme_map.items():
                if any(w in kw for w in words):
                    themes.add(theme)
        if not themes:
            themes.add('Other')
        for theme in themes:
            results.append({'bank': bank, 'theme': theme})
    themes_df = pd.DataFrame(results)
    themes_df.to_csv(output_csv, index=False)
    print(f"Themes grouped and saved to {output_csv}")

if __name__ == "__main__":
    group_themes("data/bank_keywords.csv", "data/bank_themes.csv")
