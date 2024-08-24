from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a72b2bd403ed74e86db3ac5ada8c6ab0'

# with open('posts.json', 'r') as file:
# 	posts_dict = json.load(file)

posts = [
    {
        'author': 'The Weeknd',
        'title': 'Out of Time',
        'content': 'First best post',
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
    return render_template("home.html", posts=posts, title='Home')

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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


if __name__ == "__main__":
    app.run(debug=True)
    