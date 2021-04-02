# Project 3 Flask application

| <a href="https://github.com/DamianMcNulty/project3quiz/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/project3quiz.svg?style=social" alt="GitHub stars"> </a> | [![Travis CI Testing](https://travis-ci.org/DamianMcNulty/project3quiz.svg?branch=master)](https://travis-ci.org/DamianMcNulty/project3quiz) | 
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |

## Goal

> To create a Quiz Game using a python and flask web application

## Description

## UX

### Game

1.  The user enters a username and submits a form
2.  The user name is checked for uniqueness
3.  The user must enter a username to play a game
4.  The user is presented with a riddle
5.  The user enters their answer into a textarea
6.  The user submits the answer using a form
7.  If the answer is correct the next riddle is presented
8.  If the answer is incorrect the guess is stored and printed below the riddle and the textarea is cleared
9.  Top scores for all users are displayed in a leaderboard

### User Stories

1.  As a user, I want to create a username so that I can play a game
2.  As a user, I want to submit my username so that I can start a game
3.  As a user, I want to solve a coding challenge so that can I play a game
4.  As a user, I want to submit my answer to the challenge so that I can play a game
5.  As a user, I want solve the next challenge so that I can play a game
6.  As a user, I want to keep my score so that I know how I have played
7.  As a user, I want to view the leaderboard so that I can compare how I have played a game to other users

### Wireframes

see wireframes folder

[Behance](https://www.behance.net/gallery/80996291/Java-Quiz) 

## Technologies Used

1.  [HTML5](https://en.wikipedia.org/wiki/HTML5)
2.  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
3.  [Git](https://git-scm.com/)
4.  [Github](https://github.com/)
5.  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
6.  [Python 3.9.1](https://www.python.org/)
7.  [AdobeXD](https://www.adobe.com/ie/products/xd.html)
8.  [Online Converter](https://www.onlineconverter.com/mp4-to-gif)
9.  [Cross Browser Testing](https://crossbrowsertesting.com/)
10. [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/#)
11. [JQuery 3.6.0](https://jquery.com/)
12. [DataTables 1.10.24](https://github.com/DataTables/DataTables)

## Local development

Windows

    setx /m DEVELOPMENT True
    setx /m SECRET_KEY "..."
    setx /m MONGO_DBNAME "..."
    setx /m MONGO_URI "..."
    setx /m PORT 8080
    pip install virtualenv
    python -m virtualenv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    python runserver.py
    .\env\Scripts\deactivate

## connect to database

    pip install pymongo Flask-PyMongo
    pip3 freeze --local > requirements.txt

## Local Backend testing

    python test.py
    pip install coverage
    coverage run --include=./runserver.py test.py
    coverage report
    coverage html

## Cross Browser testing

see screenshots in cbt folder

## Research

-   <https://www.reddit.com/r/learnpython/comments/1hsxxy/faviconico_get_request_in_flask/>
-   <https://stackoverflow.com/questions/30333299/pymongo-bson-convert-python-cursor-cursor-object-to-serializable-json-object>

## Deployment

    sudo pip3 install flask
    pip3 freeze --local > requirements.txt
    heroku login
    heroku create damianmcdev1-project3quiz --region eu
    echo web: python runserver.py > Procfile
    heroku config:set IP="0.0.0.0"
    heroku config:set PORT="8080"
    git push heroku master

## Credits

## License

See [LICENSE](LICENSE).