from flask_blog import app, db, brcypt
from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

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
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check username and password', 'danger')
    return render_template("login.html", form=form, title='Login')