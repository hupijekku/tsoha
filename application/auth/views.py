from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.posts.models import Post, Vote, PostTag
from application.auth.forms import LoginForm, RegisterForm, UpdateForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout/")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    error = ""
    if request.method == "GET":
        return render_template("auth/register.html", form = RegisterForm(), perr = error)

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form, perr = error)
    user = User.query.filter_by(username=form.username.data).first()

    if user:
        error = "Username already taken."
        return render_template("auth/register.html", form = form, perr = error)

    u = User(form.full_name.data, form.username.data, form.password.data, "USER", False)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/account", methods = ["GET", "POST"])
@login_required(role="USER")
def auth_mypage():
    if request.method == "GET":
        return render_template("auth/user.html", form = UpdateForm())

    error = ""
    form = UpdateForm(request.form)

    if not form.validate():
        return render_template("auth/user.html", form = form, perr = error)
   
    if not form.current_password.data == current_user.password:
        error = "Current password doesn't match"
        return render_template("auth/user.html", form = form, perr = error)
    
    user = User.query.filter_by(username=form.username.data).first()
    if user and not form.username.data == current_user.username:
        error = "Username already taken"
        return render_template("auth/user.html", form = form, perr = error)

    # Current password and validation passed, update user data
    user = User.query.get(current_user.id)
    user.full_name = form.full_name.data
    user.username = form.username.data
    user.password = form.password.data
    
    db.session().commit()

    return redirect(url_for("index"))

@app.route("/auth/delete", methods = ["POST"])
@login_required(role="USER")
def auth_delete():
    user = User.query.get(current_user.id)
    posts = Post.query.filter_by(user_id=current_user.id)
    for post in posts:
        db.session().delete(post)
        votes1 = Vote.query.filter_by(post_id = post.id)
        for vote in votes1:
            db.session().delete(vote)
        posttags = PostTag.query.filter_by(post_id = post.id)
        for posttag in posttags:
            db.session().delete(posttag)
    votes2 = Vote.query.filter_by(user_id = user.id)
    for vote in votes2:
        db.session().delete(vote)
    db.session().delete(user)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/auth/list", methods = ["GET"])
def auth_list():
    users = User.query.all()

    return render_template("auth/list.html", users = users)
