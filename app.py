from flask import Flask
import pandas as pd

# read in csv data
df = pd.read_csv("wnbadraft.csv")

# create a random starting lineup
lineup = df.sample(n=5)

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"
