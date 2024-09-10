import os
import secrets
from PIL import Image
from flask_blog import app, db, brcypt
from flask import render_template, url_for, flash, redirect, request
from flask_blog.forms import RegistrationForm, LoginForm, UpdateForm
from flask_blog.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

# with open('posts.json', 'r') as file:
# 	posts_dict = json.load(file)

posts_not_use = [
    {
        'author': 'The Weeknd',
        'title': 'Out of Time',
        'content': 'First best song',
        'date_released': '12-02-2022'
    },
    {
        'author': 'Abel Makkonen',
        'title': 'Heartless',
        'content': 'Second best song',
        'date_released': '12-02-2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts_not_use, title='Home')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/makk')
def makk():
    return render_template("makk.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = brcypt.generate_password_hash(form.password.data).decode('utf-8') # Hash the password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # add user data
        db.create_all()
        db.session.add(user)
        db.session.commit() # Add and commit changes to the db
        flash(f'Your account has been created. You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        #     flash('You have been logged in!', 'success')
        user = User.query.filter_by(email=form.email.data).first() # Returns first results or None if email is invalid
        if user and brcypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)       # login_user manages the log in process
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check email and password', 'danger')
    return render_template("login.html", form=form, title='Login')

@app.route('/logout') # Display the logout nav
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_pic(form_picture):
    random_hex = secrets.token_hex(8)   # For filename
    _, f_ext = os.path.split(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_resize = (125, 125)
    new_image = Image.open(form_picture)
    new_image.thumbnail(output_resize)
    new_image.save(picture_path)

    return picture_fn

@app.route('/account', methods=['GET', 'POST'])   # Display account
@login_required
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_pic(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated succesfully!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename = f"profile_pics/{current_user.image_file}")
    return render_template("account.html", image_file=image_file, form=form, title="Account")