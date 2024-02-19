from flask import render_template, request, redirect, url_for
from app.models import  Student, db
# you write view functions
from app.students import student_blueprint


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
        # std = Student(name=request.form['name'], age=request.form['age'],
        #               image=request.form['image'], grade=request.form['grade'])
        # db.session.add(std)
        # db.session.commit()
        # return redirect(url_for('students.index'))

        student = Student.save_student(request.form)
        return redirect(student.show_url)

    return render_template("students/create.html")
