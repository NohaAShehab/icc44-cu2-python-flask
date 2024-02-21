from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    # db.relationship (modelname )
    students = db.relationship('Student', backref='track_name', lazy=True)
    # students contains students in this track

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def get_all_tracks(cls):
        return cls.query.all()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    grade= db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    # add track to student
    track_id =db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=True)


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

    @classmethod
    def save_student(cls, request_data):  # immutable dict
        student = cls(**request_data)
        db.session.add(student)
        db.session.commit()
        return student

    @classmethod
    def delele_student(cls, id):
        std = cls.query.get_or_404(id)
        db.session.delete(std)
        db.session.commit()
        return True



