from flask_restful import Resource, fields, marshal_with

from app.models import Student
from app.students import  student_blueprint

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


