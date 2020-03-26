from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.posts.models import Post
from application.posts.forms import PostForm

@app.route("/posts", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/new/")
@login_required
def posts_form():
    return render_template("posts/new.html", form = PostForm())

@app.route("/posts/<post_id>/", methods=["POST"])
@login_required
def posts_vote(post_id):
    p = Post.query.get(post_id)
    p.votes += 1
    db.session().commit()

    return redirect(url_for("posts_index"))

@app.route("/posts/", methods=["POST"])
@login_required
def posts_create():
    form = PostForm(request.form)

    if not form.validate():
        return render_template("posts/new.html", form = form)

    p = Post(form.name.data, form.content.data)
    p.user_id = current_user.id

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("posts_index"))
