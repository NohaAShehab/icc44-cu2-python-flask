

from flask_wtf import FlaskForm
from wtforms import  StringField, IntegerField
from wtforms.validators import DataRequired
class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField("Image")
    age = IntegerField("Age", validators=[DataRequired()])
    grade = IntegerField("Grade", validators=[DataRequired()])

