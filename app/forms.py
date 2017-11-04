from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired


class LoginForm(Form):
    """Login form to access yarn and user details pages"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(Form):
    """User registration form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class YarnersForm(Form):
    """Yarners listing form"""
    yarner = StringField('Name', validators=[DataRequired()])
    hibiscus = IntegerField('Hibiscus', validators=[DataRequired()])
    existingYarns = SelectField(
        'Existing Yarns', 
        choices = []
    )

