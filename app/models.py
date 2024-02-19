from flask_sqlalchemy import SQLAlchemy


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

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()
