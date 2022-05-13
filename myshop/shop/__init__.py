from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager, current_user, logout_user, login_required
from flask_migrate import Migrate
import uuid

import os

def gen_rand_val():
    rand_val = uuid.uuid4().hex
    return rand_val

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY']= gen_rand_val()
app.permanent = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True




# os.environ.get("SECRET_KEY", "thisisforlocal")
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static/img')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.refresh_view = "user.reauthenticate"
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)

migrate = Migrate(app, db)

from .admin import models
from .products import models

app.app_context().push()
db.create_all()

from .admin import urls
from .products import urls
from .customers import urls
from .carts import urls