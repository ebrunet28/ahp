from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Aon Hockey Pool", posts=posts)


@app.route("/ranking")
def ranking():
    return render_template("ranking.html", title="Ranking")


@app.route("/historical")
def historical():
    return render_template("historical.html", title="Historical")


@app.route("/statement")
def statement():
    return render_template("statement.html", title="Statement")


@app.route("/transaction")
def transaction():
    return render_template("transaction.html", title="Transaction")


@app.route("/unit")
def unit():
    return render_template("unit.html", title="Unit")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
