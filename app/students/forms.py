

from flask_wtf import FlaskForm
from wtforms import  StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import  QuerySelectField
from app.models import Track

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField("Image")
    age = IntegerField("Age", validators=[DataRequired()])
    grade = IntegerField("Grade", validators=[DataRequired()])
    # add track field --> one to many ---> get data from another model
    track = QuerySelectField("Track", query_factory=lambda:Track.get_all_tracks())
