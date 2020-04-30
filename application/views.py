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
    top_posts = []
    c = 0
    for row in res:
        if c < 10:
            top_posts.append({"full_name": row[0], "count":row[1]})
            c += 1
        else:
            break

    stmt = text("SELECT DISTINCT tag.name, COUNT(*) as c FROM post_tag LEFT JOIN tag ON tag_id = tag.id GROUP BY tag.name ORDER BY c DESC")
    res = db.engine.execute(stmt)
    top_tags = []
    c = 0
    for row in res:
        if c < 10:
            top_tags.append({"name": row[0], "count": row[1]})
            c += 1
        else:
            break
    
    stmt = text("SELECT post.id, post.title, COUNT(vote.post_id) as c FROM vote LEFT JOIN post ON vote.post_id = post.id GROUP BY post.id, post.title ORDER BY c DESC")
    res = db.engine.execute(stmt)
    top_votes = []
    c = 0
    for row in res:
        if c < 10:
            top_votes.append({"id": row[0], "title": row[1], "count": row[2]})
            c += 1
        else:
            break

    return render_template("index.html", top_posters=top_posts, top_tags=top_tags, top_votes=top_votes)
