from flask_wtf import Form
from wtforms import StringField, BooleanField,  TextAreaField, SelectMultipleField, SelectField
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from .models import Events

class EventsForm(Form):
    date=DateField('date', validators=[DataRequired()])
    title=StringField('title', validators=[DataRequired()])
    description=StringField('description', validators=[DataRequired()])
