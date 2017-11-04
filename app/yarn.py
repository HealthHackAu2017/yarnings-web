from flask_wtf import FlaskForm as Form
from wtforms import StringField, BooleanField
from wtforms.validators import Optional, DataRequired

class Yarn():
    

class YarnForm(Form):
    """Yarn form to hold and share a yarning"""
    preferred_name = StringField('Name', validators=[Optional()])
    ajax = BooleanField('Ajax', validators=[DataRequired()])
