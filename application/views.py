# Tuodaan Flask ja app
from flask import render_template
from application import app

# Default route, renderöidään aloitussivu
@app.route("/")
def index():
    return render_template("index.html")
