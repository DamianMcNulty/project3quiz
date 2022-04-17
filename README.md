# Project 3 Flask application

| <a href="https://github.com/DamianMcNulty/project3quiz/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/project3quiz.svg?style=social" alt="GitHub stars"> </a> | [![CircleCI](https://circleci.com/gh/DamianMcNulty/project3quiz/tree/master.svg?style=shield)](https://circleci.com/gh/DamianMcNulty/project3quiz/tree/master) | 
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |

## Goal

> To create a Quiz Game using a python and flask web application

## Description

## UX

### User Stories

1.  As a user, I want to create a username which is between 6 and 10 letters or digits long, does not contain spaces and does not begin with a digit so that I can submit my username to start a game.
2.  As a user, I want to solve a coding challenge and check my answer so that I can score a point
3.  As a user, I want solve the next challenge or finish the game
4.  As a user, I want to know how my score as I play the game
5.  As a user, I want to view the leaderboard so that I can compare how I have played a game to other users

### Wireframes

see wireframes folder

[Behance](https://www.behance.net/gallery/80996291/Java-Quiz) 

## Technologies Used

1.  [HTML5](https://en.wikipedia.org/wiki/HTML5)
2.  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
3.  [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
4.  [Python 3.9.1](https://www.python.org/)
5. [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/#)
6. [JQuery 3.6.0](https://jquery.com/)
7. [DataTables 1.10.24](https://github.com/DataTables/DataTables)

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
