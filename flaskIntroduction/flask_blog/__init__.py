from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a72b2bd403ed74e86db3ac5ada8c6ab0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
brcypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


from flask_blog.main.routes import main
from flask_blog.users.routes import users
from flask_blog.posts.routes import posts   # Import the Blueprint

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts) # Register the blueprints


# 1. Import Blueprint
# 2. Restructure modules into specific related packages
# 3. Restructure import statements..
# 4. change url_for() functions to include blueprint module file_names
# 5.  Change login
# 6. Test the changes..