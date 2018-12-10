from flask import Flask, render_template, request, flash, redirect, url_for, session
from os import environ
import json
from datetime import datetime

app = Flask(__name__)

app.secret_key = '7l8/%Zb'

names = []
user = []

score = 0
question = 0
users = []

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/', methods=["GET", "POST"])
@app.route('/home')
def home():
    """Renders the home page."""
    if request.method == "POST":
        if request.form["name"] in names:
            message = "The user name " + request.form["name"] + " has already been taken"
            flash(message)
            return render_template('index.html', title='Home Page', year=datetime.now().year)
        else:
            names.append(request.form["name"])
        return redirect(request.form["name"])
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/<name>', methods=["GET", "POST"])
def game(name):
    data = []
    with open("data/data.json", "r") as json_data:
        data = json.load(json_data)
    global question
    global score
    if request.method == "POST" and request.form["answer"] == data[question]['answer']:
        score += 1
        question += 1
        user.append({"name": name, "score": score})
        return redirect('/' + name)
    if request.method == "POST" and request.form["answer"] != data[question]['answer']:
        message = "Answer " + request.form["answer"] + " is incorrect, please try again."
        flash(message)
        return redirect('/' + name)
    return render_template("game.html", page_title = "Java Quiz", data=data[question], name=name, score=score, question=question, year=datetime.now().year)


@app.route('/leaderboard', methods=["GET"])
def leaderboard():
    """Renders the leaderboard."""
    global user
    return render_template(
        'leaderboard.html',
        title='Leaderboard',
        year=datetime.now().year,
        message='Leaderboard', 
        scores = user
    )

if environ.get('DEVELOPMENT'):
    development = True
else:
    development = False

if __name__ == '__main__':
    HOST = environ.get('IP')
    if development:
        PORT = int(environ.get('C9_PORT'))
    else:
        PORT = int(environ.get('PORT'))
    app.run(HOST, PORT, debug=development)