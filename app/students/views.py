from flask import render_template
from app.models import  Student
# you write view functions


def students_index():
    students = Student.get_all_objects()
    # render data to the template
    return  render_template("students/index.html", students=students)
