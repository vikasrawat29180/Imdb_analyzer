import pandas as pd
from pathlib import Path
report = []
report.append("IMDb Movies Data Analyzer - Report")
report.append("="*40)
df = pd.read_csv("imdb_cleaned.csv")
report.append(f"Total movies: {len(df)}")
report.append("\nTop 5 movies by rating:")
report.append(df.sort_values('rating', ascending=False)[['title','year','rating']].head().to_string(index=False))
report.append("\nDirector stats (top 5 by box office millions):")
report.append(pd.read_csv('director_stats.csv').head().to_string(index=False))
report_path = Path("imdb_report.txt")
report_path.write_text("\n\n".join(report))
print("Report saved to imdb_report.txt")