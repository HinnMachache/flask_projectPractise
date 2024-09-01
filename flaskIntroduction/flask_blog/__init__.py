from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a72b2bd403ed74e86db3ac5ada8c6ab0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flask_blog import routes
