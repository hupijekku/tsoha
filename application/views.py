# Tuodaan Flask ja app
from flask import render_template
from application import app, db
from application.auth.models import User
from application.posts.models import Post, Vote

from sqlalchemy.sql import text

# Default route, renderöidään aloitussivu
@app.route("/")
def index():

    stmt = text("SELECT account.full_name, COUNT(account.id) as c FROM account LEFT JOIN post ON account.id = post.user_id WHERE post.title IS NOT NULL GROUP BY account.id, post.user_id ORDER BY c DESC")
    res = db.engine.execute(stmt)
    response = []
    for row in res:
        response.append({"full_name": row[0], "count":row[1]})

    return render_template("index.html", top_posters=response)
