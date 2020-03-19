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

# Luodaan tietokantataulut
db.create_all()
