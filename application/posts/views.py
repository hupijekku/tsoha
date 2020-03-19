from application import app, db
from flask import redirect, render_template, request, url_for
from application.posts.models import Post


@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/new/")
def posts_form():
    return render_template("posts/new.html")

@app.route("/posts/<post_id>/", methods=["POST"])
def posts_vote(post_id):
    p = Post.query.get(post_id)
    p.votes += 1
    db.session().commit()

    return redirect(url_for("posts_index"))

@app.route("/posts/", methods=["POST"])
def posts_create():
    p = Post(request.form.get("title"), request.form.get("content"))

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("posts_index"))
