import os
import secrets
from PIL import Image
from flask_blog import app, db, brcypt
from flask import render_template, url_for, flash, redirect, request
from flask_blog.forms import RegistrationForm, LoginForm, UpdateForm, PostForm
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


