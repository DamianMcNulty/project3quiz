# Project 3 Flask application

| <a href="https://github.com/DamianMcNulty/project3quiz/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/project3quiz.svg?style=social" alt="GitHub stars"> </a> 	| [![Travis CI Testing](https://travis-ci.org/DamianMcNulty/project3quiz.svg?branch=master)](https://travis-ci.org/DamianMcNulty/project3quiz) 	|
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------	|

## Goal
>To create a Quiz Game using a python and flask web application

## Table of Contents
- [Description](#description)
- [UX](#ux)
- [Technologies Used](#technologies-used)
    - HTML5
    - CSS3
    - Python
    - Flask
- [Local Testing](#local-testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)
- [LICENSE](#license)

## Description
[(Back to top)](#table-of-contents)

## UX
[(Back to top)](#table-of-contents)
### Game
1. The user enters a username and submits a form
2. The user name is checked for uniqueness
3. The user must enter a username to play a game
4. The user is presented with a riddle
5. The user enters their answer into a textarea
6. The user submits the answer using a form
7. If the answer is correct the next riddle is presented
8. If the answer is incorrect the guess is stored and printed below the riddle and the textarea is cleared
9. Top scores for all users are displayed in a leaderboard

### User Stories
1. As a user I want to create a username so that I can play a game
2. As a user I want to submit my username so that I can start a game
3. As a user I want to solve a puzzle/coding challenge so that can I play a game
4. As a user I want to submit my answer to the puzzle/challenge so that I can play a game
5. As a user I want solve the next puzzle/challenge so that I can play a game
6. As a user I want to keep my score so that I know how I have played
7. As a user I want to view the leaderboard so that I can compare how I have played a game to other users
## Technologies Used
[(Back to top)](#table-of-contents)
1. [![HTML5](https://github.com/DamianMcNulty/my-first-website/blob/master/img/HTML5_logo_and_wordmark.svg)](https://en.wikipedia.org/wiki/HTML5) 

2. [![CSS3](https://github.com/DamianMcNulty/my-first-website/blob/master/img/CSS3_logo_and_wordmark.svg)](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  

3. [![Git](https://github.com/DamianMcNulty/my-first-website/blob/master/img/Git-logo.svg)](https://en.wikipedia.org/wiki/Git)

4. [![JavaScript](https://github.com/DamianMcNulty/my-first-website/blob/master/img/Unofficial_JavaScript_logo_2.svg)](https://en.wikipedia.org/wiki/JavaScript)

## Local testing
```pip install virtualenv
   python -m virtualenv env
   .\env\Scripts\activate
   pip install -r requirements.txt
   python runserver.py
   .\env\Scripts\deactivate
```

Cloud9
```
    pip3 install -r requirements.txt
    export DEVELOPMENT=1
    python3 runserver.py
```

## Research
[(Back to top)](#table-of-contents)
1. https://www.reddit.com/r/learnpython/comments/1hsxxy/faviconico_get_request_in_flask/

## Deployment
[(Back to top)](#table-of-contents)
1. sudo pip3 install flask
2. pip3 freeze --local > requirements.txt
1. heroku login
2. heroku create damianmcdev1-project3quiz --region eu
3. echo web: python runserver.py > Procfile
4. heroku config:set IP="0.0.0.0"
5. heroku config:set PORT="8080"
6. git push heroku master

 
## Credits
[(Back to top)](#table-of-contents)

## License:

See [LICENSE](LICENSE).
