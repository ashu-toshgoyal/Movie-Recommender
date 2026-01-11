import pandas as pd

def searchMovie(x):
    df = pd.read_csv("database.csv")
    

searchMovie(2001)
# searchMovie(2011)


# y = "Sharukh Khan Ki movie Pathaan"
# bs = 50
# for i in y.split():
#     if i.lower() == "sharukh" or i.lower() == "pathan":
#         bs+=10
#         print(bs)
