from flask import Flask, render_template, request
import lib
from collections import defaultdict

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/combinations/<letters>")
def combination(letters):
    tiles = list(letters)
    words = lib.find_words(tiles, matches=set())
    scores = defaultdict(list)
    for word in words:
        scores[lib.get_score(word)].append(word)

    return render_template(
        "combination.html",
        combination=tiles,
        total_words=sorted(scores.items(), key=lambda item: item[0], reverse=True),
        str=str,
    )


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)