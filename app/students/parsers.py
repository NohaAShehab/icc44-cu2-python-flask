# define parser to convert request.data to python datatypes

from flask_restful import reqparse

students_parser = reqparse.RequestParser()
students_parser.add_argument('name', type=str, required=True, help="Name is required")
students_parser.add_argument('image', type=str)
students_parser.add_argument('age',type=int)
students_parser.add_argument('grade', type=int)
students_parser.add_argument('track_id', type=int)