import pandas as pd
df = pd.read_csv("imdb_cleaned.csv")
grp = df.groupby('director').agg(
    movie_count=('title','count'),
    avg_rating=('rating','mean'),
    total_box_office_millions=('box_office_millions','sum')
).reset_index().sort_values('total_box_office_millions', ascending=False)
grp.to_csv("director_stats.csv", index=False)
print("Director stats saved to director_stats.csv")
print(grp)