from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    """ Login form to access yarn and user details pages """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    ajax = BooleanField('Ajax', validators=[DataRequired()])

class RegisterForm(Form):
    """ User registration form """
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    ajax = BooleanField('Ajax', validators=[DataRequired()])

class YarnersForm(Form):
    """ Yarners listing form """
    yarners = SelectField('Existing Yarns')

class NewYarnerForm(Form):
    """ New Yarner form """
    name = StringField('Name', validators=[DataRequired()])
    hibiscus = IntegerField('Hibiscus', validators=[DataRequired()])
    ajax = BooleanField('Ajax', validators=[DataRequired()])

class ProfileForm(Form):
    """ Helpers profile form """
    email = StringField('Email', validators=[Email()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    ajax = BooleanField('Ajax', validators=[DataRequired()])
