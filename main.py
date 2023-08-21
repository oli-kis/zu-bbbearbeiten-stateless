import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

# Hier wird eine URL definiert


@app.route("/")
def index():
    todos = helper.get_all()
    # Hier werden die Daten an "index.html" übergeben.
    return render_template('index.html', items=todos)

# Hier wird eine URL definiert


@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("text")
    helper.add(title)
    return redirect(url_for("index"))

# Hier wird eine URL definiert


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
