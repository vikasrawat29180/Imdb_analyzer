import pandas as pd
df = pd.read_csv("imdb_cleaned.csv")
top = df.sort_values('rating', ascending=False).head(10)
top.to_csv("top_rated_movies.csv", index=False)
print("Top rated movies saved to top_rated_movies.csv")
print(top[['title','year','rating']])