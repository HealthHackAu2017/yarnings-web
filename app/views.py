from app import app, lm
from flask import request, redirect, render_template, url_for, flash, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user
from json import dumps as jsonDumps

from .forms import LoginForm, RegisterForm, YarnersForm, ProfileForm, NewYarnerForm
from .helper import Helper

ajaxOK = jsonDumps({'success':True}), 200, {'ContentType':'application/json'} 
ajaxFail = jsonDumps({'success':False}), 500, {'ContentType':'application/json'}

def ajaxOK(msg):
    return ajaxMsg(msg, 200)

def ajaxFail(msg):
    return ajaxMsg(msg, 500)

def ajaxMsg(msg, status):
    return jsonDumps({'message':msg}), status, {'ContentType':'application/json'}

@app.route('/')
def home():
    if current_user.is_authenticated:
        yarnersForm = YarnersForm()
        profileForm = ProfileForm(email=current_user.email, name=current_user.name)
        newYarnersForm = NewYarnerForm()
        helper = current_user
        return render_template('menu.html', title='Yarnings', yarnersform=yarnersForm, profileform=profileForm, newyarnerform=NewYarnerForm, helper=helper)
    loginForm = LoginForm()
    registerForm = RegisterForm()
    return render_template('home.html', title='Yarnings', loginform=loginForm, registerform=registerForm)

@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = form.username.data
        password = form.password.data
        email = form.email.data
        name = form.name.data
        tHelper = Helper(user, email, name)

        if (tHelper.insertDB(password)):
            flash("Account created successfully", category='success')
            user = app.config['HELPERS_COLLECTION'].find_one({"_id": form.username.data})
            user_obj = Helper(user['_id'], user['email'], user['name'])
            login_user(user_obj)
            if (form.ajax.data == "True"):
                return ajaxOK("Registration Successful!");
            return redirect(request.args.get("next") or url_for("home"))
        return ajaxFail("Username already registered")
    #flash("Bad input. Please check fields.", category='error')
    return ajaxFail("Failed to validate fields. Please check input.")

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = app.config['HELPERS_COLLECTION'].find_one({"_id": form.username.data})
        if user and Helper.validate_login(user['password'], app.config['SALT'] + form.password.data):
            user_obj = Helper(user['_id'], user['email'], user['name'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            if (form.ajax.data == "True"):
                return ajaxOK("Login Successful!");
            else:
                return redirect(request.args.get("next") or url_for("home"))
        if (form.ajax.data == "True"):
            return ajaxFail("Wrong username or password")
        else:
            flash("Wrong username or password", category='error')
            loginForm = LoginForm()
            registerForm = RegisterForm()
            return redirect(url_for("home"))
    flash("Bad input. Please check fields.", category='error')
    return ajaxFail
  
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/yarn', methods=['GET'])
@login_required
def yarn():
    return render_template('example.html')

@app.route('/profile-update', methods=['POST'])
@login_required
def profile_update():
    form = ProfileForm()
    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        name = form.name.data

        if (current_user.update(email, name, password)):
            flash("Profile successfully", category='success')
            user = app.config['HELPERS_COLLECTION'].find_one({"_id": current_user.get_id()})
            user_obj = Helper(user['_id'], user['email'], user['name'])
            login_user(user_obj)
            if (form.ajax.data == "True"):
                return ajaxOK("Profile updated successful!");
            return redirect(request.args.get("next") or url_for("home"))
        return ajaxFail("Failed to update profile")
    #flash("Bad input. Please check fields.", category='error')
    return ajaxFail("Failed to validate fields. Please check input.")

@app.route('/yarn-update', methods=['POST'])
@login_required
def yarn_update():
    form = YarnForm()
    if form.validate_on_submit():
        yarn

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

@app.route('/plugin/<path:path>')
def send_plugin(path):
    return send_from_directory('plugin', path)

@lm.user_loader
def load_user(username):
    u = app.config['HELPERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return Helper(u['_id'], u['email'], u['name'])
