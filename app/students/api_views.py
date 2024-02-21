from flask_restful import Resource, fields, marshal_with
from flask import request
from app.models import Student, db
from app.students import  student_blueprint
from app.students.parsers import  students_parser

@student_blueprint.route("/api", endpoint="api")
def get_students():
    students = Student.query.all()
    # serlization ? ---> convert object my sql_alchemy to list of dicts
    stds = []
    for std in students:
        std_data =std.__dict__
        del std_data["_sa_instance_state"]
        stds.append(std_data)
    print(stds)
    # return students  #     Object of type Student is not JSON serializable
    return stds

track_serilizer= {
    "id": fields.Integer,
    "name":fields.String
}

student_serilizer = {
    "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
    "grade": fields.Integer,
    "age":fields.Integer,
    "track_id": fields.Integer,
    "track_name": fields.Nested(track_serilizer)
}

class StudentList(Resource):
    @marshal_with(student_serilizer)
    def get(self):
        students = Student.query.all()
        return students , 200

    @marshal_with(student_serilizer)
    def post(self):
        print(request.data)  # get data from request.data  ==> string
        # I need to parse these data to python datatypes
        student_data = students_parser.parse_args()
        print(student_data)
        student = Student.save_student(student_data)
        # return  student.id
        return student , 201




## crud operation on student // show , edit , delete
class StudentResource(Resource):
    @marshal_with(student_serilizer)
    def get(self, std_id):
        student = Student.get_student_by_id(std_id)
        return student, 200

    @marshal_with(student_serilizer)
    def put(self, std_id):
        student = Student.get_student_by_id(std_id)
        if student:
            student_data = students_parser.parse_args()
            student.name = student_data["name"]
            student.image = student_data["image"]
            student.grade =student_data["grade"]
            student.age = student_data["age"]
            student.track_id =student_data["track_id"]
            db.session.add(student)
            db.session.commit()
            return student




    def delete(self, std_id):
        deleted = Student.delele_student(std_id)
        return deleted, 204
