from flask_sqlalchemy import SQLAlchemy
from flask import url_for


db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    grade= db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)


    def __str__(self):
        return self.name


    @property
    def image_url(self):
        return url_for('static', filename=f'students/images/{self.image}')

    @property
    def show_url(self):
        return url_for("students.show", id = self.id)

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()

    @classmethod
    def get_student_by_id(cls, id):
        return  cls.query.get_or_404(id)



