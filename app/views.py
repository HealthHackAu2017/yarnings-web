from app import app, lm
from flask import request, redirect, render_template, url_for, flash, send_from_directory
from flask.ext.login import login_user, logout_user, login_required

from werkzeug.security import generate_password_hash
from pymongo.errors import DuplicateKeyError

from .forms import LoginForm, RegisterForm
from .user import User, RegisterUser


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm
    if request.method == 'POST' and form.validate_on_submit():
        # Ask for data to store
        user = form.username.data
        password = form.password.data
        pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert the user in the DB
        try:
            collection.insert({"_id": user, "password": pass_hash})
            flash("Account created successfully", category='success')
            return redirect(url_for("menu"))
        except DuplicateKeyError:
            flash("User ", category='error')
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("menu"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)

@app.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/yarn', methods=['GET', 'POST'])
@login_required
def yarn():
    return render_template('example.html')


@app.route('/details', methods=['GET', 'POST'])
@login_required
def details():
    return render_template('details.html')

#### static (move to nginx in prod)
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/lib/<path:path>')
def send_lib(path):
    return send_from_directory('lib', path)

@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
