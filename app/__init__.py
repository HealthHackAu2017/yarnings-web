from flask import Flask, session
from flask_login import LoginManager
from flask.ext.session import Session


app = Flask(__name__)
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
SESSION_TYPE = 'filesystem'
#Session(app)

from app import views
