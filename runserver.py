from os import environ
import json
from bson.json_util import dumps
from datetime import datetime

from flask import Flask, render_template, request, flash, redirect, session

from flask_pymongo import PyMongo

app = Flask(__name__)

app.secret_key = environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = environ.get('MONGO_URI')

mongo = PyMongo(app)

names = []
user = []
number_of_questions = 6

@app.route('/')
def index():
    session.pop('user', None)
    session['login'] = True
    session['data'] = json.loads(dumps(list(mongo.db.questions.find())))
    return render_template(
        'index.html',
        title='Start',
        year=datetime.now().year,
    )

@app.route('/leaderboard')
def leaderboard():
    if 'user' not in session:
        return redirect('/')
    for n in user:
        if n['name'] == session['user']:
          user.remove(n)
    user.append({"name": session['user'], "score": session['score']})
    return render_template(
        'leaderboard.html',
        title='Leaderboard',
        year=datetime.now().year,
        scores = user
    )

@app.route('/login', methods=["GET", "POST"])
def login():
    session.pop('login', None)
    if 'user' in session:
        return redirect('/user/' + session['user'])
    if request.method == "POST":
        if request.form["name"] in names:
            message = "The user name " + request.form["name"] + " is taken, try another username"
            flash(message)
            return render_template('login.html', title='Login in to play', year=datetime.now().year)
        else:
            if(request.form["name"] == ""):
                message = "You have not entered a username, please try again."
                flash(message)
                return redirect('/login')
            names.append(request.form["name"])
            session['user'] = request.form["name"]
            session['score'] = 0
            session['question'] = 0
            session['total'] = number_of_questions + 1
            session['gameover'] = False
        return redirect('/user/' + session['user'])
    return render_template(
        'login.html',
        title='Login to',
        year=datetime.now().year,
    )

@app.route('/user/<name>', methods=["GET", "POST"])
def game(name):
    if 'user' not in session:
        return redirect('/')
    if request.method == "POST":
        if request.form["answer"] != session['data'][session['question']]['answer']:
            message = "Answer " + request.form["answer"] + " is incorrect, please try again."
            flash(message)
            session['score'] -= 1
            return redirect('/user/' + name)
        if request.form["answer"] == session['data'][session['question']]['answer']:
            session['score'] += 1
            session['question'] += 1
            return redirect('/user/' + name)
        if request.form["skip"] == "Next":
            if(session['question'] == number_of_questions):
                session['gameover'] = True
            session['question'] += 1
            return redirect('/user/' + name)
    return render_template("game.html", title = "Game Over" if session['gameover'] else "Question " + str(session['question'] + 1), data = session['data'][session['question']], question = session['question'], year=datetime.now().year)


if environ.get('DEVELOPMENT'):
    development = True
else:
    development = False

if __name__ == '__main__':
    HOST = environ.get('IP')
    PORT = int(environ.get('PORT'))
    app.run(HOST, PORT, debug=development)
