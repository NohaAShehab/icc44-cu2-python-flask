""" import flask """
from flask import Flask
from flask import request, render_template, redirect, url_for

# configure flask _sql alchemy

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # initialize the application in the main of the current module
students = [{"id": 1, "name": "Shrouq", "image":"pic1.png"},
            {"id": 2, "name": "Ali",  "image":"pic2.png"},
            {"id": 3, "name": "mohamed",  "image":"pic3.png"}]


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
@app.route("/stds/<int:id>")
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




#serving static files ? ===>
@app.route("/students/land")
def students_land():
    return  render_template("students/landing.html", students=students)

"""manage urls """
""" by default each url you created --> end_point default --> function_name """

@app.route("/test", endpoint="test_url")
def test():
    return  "Test"

# send parm in url

@app.route("/students/<int:id>", endpoint="student.show")
def show_student(id):
    stds = list(filter(lambda student: student['id'] == id, students))
    print(stds)
    if stds:
        return render_template("students/profile.html", student=stds[0])

    return "Student not found "

#connect flask app to the database (ORM===> object relational mapper )
"""
http://127.0.0.1:5001/students/1
"""
"sqllite_"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db= SQLAlchemy(app)  # create instance folder---> contain project.db

# use db object ---> create model ---> used later in create table and crud
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)

    def __str__(self):
        return f"{self.name}"

## create model in the db
# goto shell
"""
    flask shell
    db.create_all() // create table in sql_lite db =
"""

@app.route("/products", endpoint='products.index')
def products_index():
    products = Product.query.all()
    return  render_template("products/index.html",products=products)

@app.route("/products/<int:id>", endpoint="product.show")
def products_show(id):
    # product = Product.query.get(id)
    product = Product.query.get_or_404(id)
    return render_template("products/show.html", product=product)

###### delete the object
"""
    1- get object 
    2- db.session.delete(object)
    3- db.session.commit
"""

## create form to add object
""" default while defining route --->supported  methods ===> GET"""
@app.route("/products/create",methods =['GET', 'POST'], endpoint='product.create')
def create_product():
    ## post
    print(request.form)
    if request.method == 'POST':
        product = Product(name=request.form['name'], image=request.form['image'])
        db.session.add(product)
        db.session.commit()
        # return "Saved
        return redirect(url_for('products.index'))

    ## get
    return render_template("products/create.html")











#### configure not found 404 ==
@app.errorhandler(404)
def get_404(error):
    return render_template("error404.html")


if __name__ == '__main__':
    # run the  development server
    app.run(debug=True, port=5001)

""" to run flask app from terminal

    1- export FLASK_APP=modulename
    2- export DEBUG=1
    3- flask run --port 5001  --debug
"""
