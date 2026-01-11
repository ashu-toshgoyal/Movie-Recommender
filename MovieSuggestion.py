from tkinter import *
from movie_Search import searchMovie

# Window
win = Tk()
win.geometry("750x850") 
win.minsize(500, 500)
win.configure(bg="#ffffff")
win.title("Climaz")

win.iconphoto(
    False,
    PhotoImage(file="Icon/picture_10650326.png")
)

def search_Movie():
    # print("Hello World")
    gen = mood_genre_input.get()
    Result_box.insert(END,gen)
    




# Component
heading_label = Label(
    win,
    text="Climaz",
    fg="#1d1d1f",
    bg="white",
    font=("Helvetica Neue", 34, "bold")
)
heading_label.pack(pady=(35, 6))

subtitle = Label(
    win,
    text="Mood-based recommendations, simplified",
    fg="#6e6e73",
    bg="white",
    font=("Helvetica Neue", 13)
)
subtitle.pack(pady=(0, 30))

input_frame = Frame(win, bg="white")
input_frame.pack(pady=10)

mood_genre_input = Entry(
    input_frame,
    width=42,
    fg="#1d1d1f",
    bg="#f5f5f7",
    font=("Helvetica Neue", 16),
    bd=0,
    insertbackground="#1d1d1f",
    highlightthickness=1,
    highlightcolor="grey"
)
mood_genre_input.pack(ipady=10, padx=12)

result_frame = Frame(win, bg="white")
result_frame.pack(pady=25, fill=BOTH, expand=True)

Result_box = Text(
    result_frame,
    wrap=WORD,
    fg="#1d1d1f",
    bg="#f5f5f7",
    font=("Helvetica Neue", 11),
    bd=0,
    padx=14,
    pady=14,
    highlightthickness=1,
    highlightcolor="black"
)
Result_box.pack(fill=BOTH, expand=True, padx=50)

action_frame = Frame(win, bg="white")
action_frame.pack(pady=10)

like_btn = Button(
    action_frame,
    text="👍",
    bg="#f5f5f7",
    fg="#1d1d1f",
    font=("Helvetica Neue", 16),
    bd=0,
    width=3,
    height=1,
    # cursor="hand2"
)
like_btn.pack(side=LEFT, padx=10)

dislike_btn = Button(
    action_frame,
    text="👎",
    bg="#f5f5f7",
    fg="#1d1d1f",
    font=("Helvetica Neue", 16),
    bd=0,
    width=3,
    height=1,
    # cursor="hand2"
)
dislike_btn.pack(side=LEFT, padx=10)

avg_btn = Button(
    action_frame,
    text="📊",
    bg="#f5f5f7",
    fg="#1d1d1f",
    font=("Helvetica Neue", 16),
    bd=0,
    width=3,
    height=1,
    # cursor="c "
)
fav_btn = Button(
    action_frame,
    text="❤️",
    bg="#f5f5f7",
    fg="#e11d48",
    font=("Helvetica Neue", 18),
    bd=0,
    width=3,
    height=1
)
fav_btn.pack(side=LEFT, padx=10)

avg_btn.pack(side=LEFT, padx=10)

def hover_in(e):
    e.widget.config(bg="#e5e7eb")

def hover_out(e):
    e.widget.config(bg="#f5f5f7")

for btn in (like_btn, dislike_btn, avg_btn):
    btn.bind("<Enter>", hover_in)
    btn.bind("<Leave>", hover_out)

def on_enter(e):
    sbtn.config(bg="#005ecb")

def on_leave(e):
    sbtn.config(bg="#0071e3")

sbtn = Button(
    win,
    text="Get Recommendation",
    fg="black",
    bg="#0071e3",
    activebackground="#005ecb",
    activeforeground="white",
    font=("Helvetica Neue", 13, "bold"),
    bd=0,
    padx=22,
    pady=14,
    command=search_Movie
    # cursor="hand2"
)
sbtn.pack(pady=(10, 30))

sbtn.bind("<Enter>", on_enter)
sbtn.bind("<Leave>", on_leave)

win.mainloop()
