from flask import Blueprint
from flask_blog import db
from flask import render_template, url_for, flash, redirect
from flask_blog.posts.forms import PostForm
from flask_blog.models import Post
from flask_login import current_user, login_required

posts = Blueprint("posts", "__name__")

@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template("create_post.html", title="Create Posts", form=form)
