import os
import secrets
from PIL import Image
from flask_blog import app

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