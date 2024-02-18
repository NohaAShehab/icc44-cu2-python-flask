""" import flask """
from flask import Flask

app = Flask(__name__)  # initialize the application in the main of the current module

# define urls/ routes or url on the application
@app.route("/")
def hello_ghaza():
    name = "ahmed"
    course = 'flask'
    print(name)
    return "<h1 style='color:red'> Hello Ghaza </h1>"

@app.route("/iti")
def hello_iti():
    return "<h1 style='color:purple;text-align:center'> Hello ITI </h1>"

@app.route('/cu')
def welcome():
    return "Welcome to cu"

if __name__ == '__main__':
    # run the  development server
    app.run(debug=True, port=5001)


""" to run flask app from terminal

    1- export FLASK_APP=modulename
    2- export DEBUG=1
    3- flask run --port 5001  --debug
"""