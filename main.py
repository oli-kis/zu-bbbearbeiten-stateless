import helper
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


# Hier wird definiert, auf welche URLs die Applikation reagiert
@app.route("/")
def index():
    items = helper.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("date")
    helper.add(text, date)

    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
