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

4. [![JavaScript](<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 630" class="Card__img">
				<rect width="630" height="630" fill="#f7df1e" />
				<path d="m423.2 492.2c12.7 20.7 29.2 36 58.4 36 24.5 0 40.2-12.3 40.2-29.2 0-20.3-16.1-27.5-43.1-39.3l-14.8-6.3c-42.7-18.2-71.1-41-71.1-89.2 0-44.4 33.8-78.2 86.7-78.2 37.6 0 64.7 13.1 84.2 47.4l-46.1 29.6c-10.1-18.2-21.1-25.4-38.1-25.4-17.3 0-28.3 11-28.3 25.4 0 17.8 11 25 36.4 36l14.8 6.3c50.3 21.6 78.7 43.6 78.7 93 0 53.3-41.9 82.5-98.1 82.5-55 0-90.5-26.2-107.9-60.5zm-209.1 5.1c9.3 16.5 17.8 30.5 38.1 30.5 19.5 0 31.7-7.6 31.7-37.2v-201.3h59.2v202.1c0 61.3-35.9 89.2-88.4 89.2-47.4 0-74.8-24.5-88.8-54.1z"
				/>
			</svg>)](https://en.wikipedia.org/wiki/JavaScript)

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
