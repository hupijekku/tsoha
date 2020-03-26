# Tuodaan Flask
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Käytetään 'posts.db' tiedostoa databasena. Sijaitsee samassa kansiossa.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
# Tulosta kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Olio jota käytetään tietokannan kyselyihin
db = SQLAlchemy(app)

# Tuodaan applications/views
from application import views

# Tuodaan tarvittavat tiedostot /posts/
from application.posts import models
from application.posts import views

from application.auth import models
from application.auth import views

# Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan tietokantataulut
db.create_all()
