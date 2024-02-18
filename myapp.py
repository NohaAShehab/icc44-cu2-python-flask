""" import flask """
from flask import Flask
from flask import request, render_template

app = Flask(__name__)  # initialize the application in the main of the current module
students = [{"id": 1, "name": "Shrouq"},
            {"id": 2, "name": "Ali"},
            {"id": 3, "name": "mohamed"}]


# define urls/ routes or url on the application
@app.route("/")
def hello_ghaza():
    name = "ahmed"
    course = 'flask'
    print(name)
    return "<h1 style='color:red'> Hello Ghaza </h1>"


@app.route("/iti")
def hello_iti():
    """ flask implicitly ---> configure request"""
    return "<h1 style='color:purple;text-align:center'> Hello ITI </h1>"


@app.route('/cu')
def welcome():
    return "Welcome to cu"


@app.route("/students")
def get_students():
    print(request)
    return students


# get student info based on passed_id in url
@app.route("/students/<int:id>")
def student_profile(id):
    # get student based on id ?
    # print(type(id))
    # for student in students:
    #     if student["id"] == id:
    #         return student
    "use filter"
    stds = list(filter(lambda student: student['id'] == id, students))
    print(stds)
    if stds:
        return stds[0]

    return "Student not found "


# register route  ===>
def customRout():
    return "===> Welcome to Custom Route ===> "


app.add_url_rule("/custom", view_func=customRout)


#open shell --->  run command on the project
# flask shell
# when open
# app.url_map
# pip install flask-shell-ipython

### templates ?
""" ----> return with template  ===> render template --> templates """

@app.route("/home")
def homepage():
    return render_template("index.html")

# send context to the template
@app.route("/stds/home")
def students_home():
    return render_template("/students/home.html",
                           name="noha", students=students)











if __name__ == '__main__':
    # run the  development server
    app.run(debug=True, port=5001)

""" to run flask app from terminal

    1- export FLASK_APP=modulename
    2- export DEBUG=1
    3- flask run --port 5001  --debug
"""
