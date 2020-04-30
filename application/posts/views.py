from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from sqlalchemy.sql import text

from application.posts.models import Post, Vote, Tag, PostTag
from application.auth.models import User
from application.posts.forms import PostForm

@app.route("/posts", methods=["GET"])
def posts_index():
    posts = Post.query.all()
    post_list = []
    for post in posts:
        print(PostTag.get_post_tags(post.id))
        post_list.append((post, User.query.get(post.user_id).full_name,
        Vote.get_post_vote_count(post.id), PostTag.get_post_tags(post.id)))
    return render_template("posts/list.html", posts = post_list)

@app.route("/posts/new/")
@login_required(role="USER")
def posts_form():
    return render_template("posts/new.html", form = PostForm())

@app.route("/posts/<post_id>/update", methods=["GET", "POST"])
@login_required(role="USER")
def posts_update(post_id):
    post = Post.query.get(post_id)
    if request.method == "GET":
        return render_template("posts/update.html", post=post, form = PostForm(), text=post.content)

    form = PostForm(request.form)

    if post.user_id != current_user.id and not current_user.admin:
        return redirect(request.referrer)

    post.content = form.content.data
    db.session().commit()

    return redirect(url_for('posts_index'))

@app.route("/posts/<post_id>/", methods=["GET", "POST"])
@login_required(role="USER")
def posts_vote(post_id):
    if request.method == "POST":
        p = Post.query.get(post_id)

        # Check if user has already voted this post
        stmt = text("SELECT id FROM vote WHERE user_id = :u_id AND post_id = :p_id").params(u_id=current_user.id, p_id=post_id)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)
        # If so, don't let the user vote again.
        if len(response) > 0:
            return redirect(url_for("posts_index"))

        # User hasn't voted yet, add a vote to 'vote' table
        v = Vote(current_user.id, p.id)
        db.session().add(v)
        db.session().commit()
    elif request.method == "GET":
        posts = Post.query.filter_by(id=post_id)
        post_list = []
        for post in posts:
            post_list.append((post, User.query.get(post.user_id).full_name, Vote.get_post_vote_count(post.id)))
        return render_template("/posts/list.html", posts = post_list)
    return redirect(url_for("posts_index"))

@app.route("/posts/<post_id>/delete", methods=["POST"])
@login_required(role="USER")
def posts_delete(post_id):
    post = Post.query.get(post_id)
    if post.user_id == current_user.id or current_user.admin:
        db.session().delete(post)
        db.session().commit()
    return redirect(request.referrer)

@app.route("/posts/", methods=["POST"])
@login_required(role="USER")
def posts_create():
    form = PostForm(request.form)

    if (form.add_tag.data):
        form.tags.append(form.tag.data)
        form.tag.data = ''
        return render_template("posts/new.html", form = form)

    if not form.validate():
        return render_template("posts/new.html", form = form)

    p = Post(form.name.data, form.content.data)
    p.user_id = current_user.id

    db.session().add(p)
    db.session().commit()


    for tag in form.tags:
        tagd = Tag.query.filter_by(name=tag).first()
        if not tagd:
            t = Tag(tag)
            db.session().add(t)
            db.session().commit()
            pt = PostTag(t.id, p.id)
        else:
            pt = PostTag(tagd.id, p.id)

        db.session().add(pt)
        db.session().commit()

    PostForm.tags = []

    return redirect(url_for("posts_index"))

@app.route("/tags/", methods=["GET"])
def tags_list():

    stmt = text("SELECT name FROM tag")
    res = db.engine.execute(stmt)
    response = []
    for row in res:
        response.append(row)
    return render_template("/posts/tags.html", tags=response)
