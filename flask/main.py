from flask import Flask, render_template, request
import lib

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/combination", methods=["post"])
def combination():
    tiles = list(request.form["tiles"])
    print(tiles)
    return render_template(
        "combination.html",
        combination=tiles,
        words=lib.find_words(tiles),
        get_definitions=lib.get_definition,
    )


if __name__ == "__main__":
    app.run("localhost", 8080)