# Tuodaan Flask
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    # Käytetään 'posts.db' tiedostoa databasena. Sijaitsee samassa kansiossa.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
    # Tulosta kaikki SQL-kyselyt
    app.config["SQLALCHEMY_ECHO"] = True

# Olio jota käytetään tietokannan kyselyihin
db = SQLAlchemy(app)

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# Tuodaan applications/views
from application import views

# Tuodaan tarvittavat tiedostot /posts/
from application.posts import models
from application.posts import views

from application.auth import models
from application.auth import views

# Kirjautuminen
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan tietokantataulut
try:
    db.create_all()
except:
    pass
