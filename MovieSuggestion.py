from tkinter import *
import pandas as pd
from movie_Search import recommend_by_text, ensure_user_score_column

current_movie = None

win = Tk()
win.geometry("750x850")
win.minsize(500, 500)
win.configure(bg="#ffffff")
win.title("Climaz")

icon = PhotoImage(file="Icon/picture_10650326.png")
win.iconphoto(False, icon)


def search_Movie():
    global current_movie

    query = mood_genre_input.get()
    Result_box.delete("1.0", END)

    result = recommend_by_text(query)

    if result is None:
        Result_box.insert(END, "No recommendations found\n")
        current_movie = None
        return

    current_movie = result.iloc[0]["movie_name"]

    for _, row in result.iterrows():
        Result_box.insert(
            END,
            f"{row['movie_name']} ({row['year']}) | Score: {row['final_score']}\n"
        )


def update_user_score(delta):
    global current_movie

    if current_movie is None:
        return

    df = pd.read_csv("database.csv")
    df = ensure_user_score_column(df)

    df.loc[df["movie_name"] == current_movie, "user_score"] += delta
    df.to_csv("database.csv", index=False)


Label(
    win,
    text="Climaz",
    fg="#1d1d1f",
    bg="white",
    font=("Helvetica Neue", 34, "bold")
).pack(pady=(35, 6))

Label(
    win,
    text="Mood-based recommendations, simplified",
    fg="#6e6e73",
    bg="white",
    font=("Helvetica Neue", 13)
).pack(pady=(0, 30))

input_frame = Frame(win, bg="white")
input_frame.pack(pady=10)

mood_genre_input = Entry(
    input_frame,
    width=42,
    fg="#1d1d1f",
    bg="#f5f5f7",
    font=("Helvetica Neue", 16),
    bd=0
)
mood_genre_input.pack(ipady=10, padx=12)

result_frame = Frame(win, bg="white")
result_frame.pack(pady=25, fill=BOTH, expand=True)

Result_box = Text(
    result_frame,
    wrap=WORD,
    fg="#1d1d1f",
    bg="#f5f5f7",
    font=("Helvetica Neue", 18),
    bd=0,
    padx=14,
    pady=14
)
Result_box.pack(fill=BOTH, expand=True, padx=50)

action_frame = Frame(win, bg="white")
action_frame.pack(pady=10)

Button(
    action_frame, text="👍", font=("Helvetica Neue", 16),
    bg="#f5f5f7", bd=0, width=3,
    command=lambda: update_user_score(+5)
).pack(side=LEFT, padx=10)

Button(
    action_frame, text="👎", font=("Helvetica Neue", 16),
    bg="#f5f5f7", bd=0, width=3,
    command=lambda: update_user_score(-5)
).pack(side=LEFT, padx=10)

Button(
    action_frame, text="📊", font=("Helvetica Neue", 16),
    bg="#f5f5f7", bd=0, width=3
).pack(side=LEFT, padx=10)

Button(
    action_frame, text="❤️", font=("Helvetica Neue", 18),
    bg="#f5f5f7", fg="#e11d48", bd=0, width=3,
    command=lambda: update_user_score(+15)
).pack(side=LEFT, padx=10)

Button(
    win,
    text="Get Recommendation",
    fg="black",
    bg="#0071e3",
    font=("Helvetica Neue", 13, "bold"),
    bd=0,
    padx=22,
    pady=14,
    command=search_Movie
).pack(pady=(10, 30))

win.mainloop()
