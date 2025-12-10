import pandas as pd
df = pd.read_csv("imdb_sample.csv")
print("Original rows:", len(df))
# Standardize column names
df.columns = [c.strip().lower() for c in df.columns]
# Convert types
df['year'] = df['year'].astype(int)
df['rating'] = df['rating'].astype(float)
df['box_office_millions'] = pd.to_numeric(df['box_office_millions'], errors='coerce')
# Fill missing genres with 'Unknown'
if 'genre' in df.columns:
    df['genre'] = df['genre'].fillna('Unknown')
# Save cleaned file
df.to_csv("imdb_cleaned.csv", index=False)
print("Saved imdb_cleaned.csv with", len(df), "rows")