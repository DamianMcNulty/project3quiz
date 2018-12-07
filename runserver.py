# import the Flask class from the flask module
from flask import Flask, render_template
from os import environ

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

# start the server with the 'run()' method
if __name__ == '__main__':
    HOST = environ.get('IP')
    PORT = int(environ.get('PORT'))
    app.run(HOST, PORT, debug=True)