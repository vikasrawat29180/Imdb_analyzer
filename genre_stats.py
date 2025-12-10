import pandas as pd
df = pd.read_csv("imdb_cleaned.csv")
grp = df.groupby('genre').agg(
    movie_count=('title','count'),
    avg_rating=('rating','mean'),
    avg_box_office_millions=('box_office_millions','mean')
).reset_index().sort_values('avg_rating', ascending=False)
grp.to_csv("genre_stats.csv", index=False)
print("Genre stats saved to genre_stats.csv")
print(grp)