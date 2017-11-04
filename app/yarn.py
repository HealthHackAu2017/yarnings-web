from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class Yarn(Form):
    """Yarn form to hold and share a yarning"""
    preferred_name = StringField('Name', validators=[DataRequired()])
