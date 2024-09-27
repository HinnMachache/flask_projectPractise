from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_blog.config import Config

# import json


db = SQLAlchemy()
brcypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    brcypt.init_app(app)
    login_manager.init_app(app)
    

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