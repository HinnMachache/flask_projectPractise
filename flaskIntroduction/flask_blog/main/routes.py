from flask import render_template, Blueprint
from flask_blog.models import Post


main = Blueprint("main", "__name__")

@main.route('/')
@main.route('/home')
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts, title='Home')

@main.route("/about")
def about():
    return render_template("about.html")

@main.route('/makk')
def makk():
    return render_template("makk.html")

@main.route('/overview')
def overview():
    return render_template("overview.html")


# https://www.blackbox.ai/share/1d6b04f2-f587-4958-a24c-2c7bb3a9cd0d
