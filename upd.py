import pandas as pd

df = pd.read_csv("IMDB-Movie-Dataset(2023-1951).csv")

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

df["base_score"] = 50

df.to_csv("IMDB-Movie-Dataset(2023-1951).csv", index=False)
