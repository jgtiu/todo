from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class NewTaskForm(FlaskForm):
    task_name = StringField('Task', validators=[DataRequired()])
    due_date = DateField('Due Date', validators=[DataRequired()])
    submit = SubmitField('Enter')