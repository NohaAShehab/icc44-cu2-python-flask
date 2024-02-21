from flask import render_template, request, redirect, url_for
from app.models import  Student, db
# you write view functions
from app.students import student_blueprint
from app.students.forms import  StudentForm


def get_index():
    return "<h1> Index </h1> "


@student_blueprint.route('', endpoint='index')
def students_index():
    students = Student.get_all_objects()
    # render data to the template
    return  render_template("students/index.html", students=students)


@student_blueprint.route("/<int:id>", endpoint="show")
def students_show(id):
    student = Student.get_student_by_id(id)
    return render_template("students/show.html", student=student)


@student_blueprint.route("/create", methods=['GET', 'POST'],
                         endpoint='create')
def create_student():
    if request.method == 'POST':
        print(f"request received > {request.form}")
        student = Student.save_student(request.form)
        return redirect(student.show_url)

    return render_template("students/create.html")


@student_blueprint.route("/createform", methods=['GET', 'POST'],
                         endpoint='createform')

def create_student_viaform():
    form = StudentForm()

    return render_template("students/createform.html", form=form)
