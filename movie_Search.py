import pandas as pd
import re

STOP_WORDS = {
    "and", "or", "the", "is", "are", "they", "do",
    "where", "movie", "film", "of", "a", "an", "to"
}

SINGLE_ACTOR_WEIGHT = 30
ACTOR_PAIR_BONUS = 100
KEYWORD_WEIGHT = 10


def ensure_user_score_column(df):
    if "user_score" not in df.columns:
        df["user_score"] = 0
    return df


def text_to_words(text):
    words = re.findall(r"\w+", str(text).lower())
    return set(w for w in words if w not in STOP_WORDS)


def extract_actors(user_words):
    actors = set()
    if "salman" in user_words:
        actors.add("salman")
    if "aamir" in user_words or "amir" in user_words:
        actors.add("aamir")
    if "shahrukh" in user_words or "srk" in user_words:
        actors.add("shahrukh")
    return actors


def recommend_by_text(user_input, top_n=5):
    df = pd.read_csv("database.csv")
    df = ensure_user_score_column(df)

    user_words = text_to_words(user_input)
    user_actors = extract_actors(user_words)

    results = []

    for _, row in df.iterrows():
        score = 0

        movie_text = f"{row['movie_name']} {row['genre']} {str(row.get('cast',''))}".lower()

        matched_actors = set()
        for actor in user_actors:
            if actor in movie_text:
                matched_actors.add(actor)
                score += SINGLE_ACTOR_WEIGHT

        if len(matched_actors) >= 2:
            score += ACTOR_PAIR_BONUS

        movie_words = text_to_words(movie_text)
        score += len(user_words & movie_words) * KEYWORD_WEIGHT

        final_score = score + row["user_score"]

        if final_score > 0:
            results.append({
                "movie_name": row["movie_name"],
                "year": row["year"],
                "genre": row["genre"],
                "final_score": final_score
            })

    if not results:
        return None

    result_df = pd.DataFrame(results)
    result_df = result_df.sort_values("final_score", ascending=False)

    return result_df.head(top_n)
