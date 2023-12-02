from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash

from models.users import User

login_blueprint = Blueprint("login", __name__, template_folder="templates")


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        print(request.form)
        email = request.form.get("email", None)
        password = request.form.get("password", None)
        # remember = bool(request.form.get("remember", False))
        user = User.query.filter(User.email == email).first()
        if not user:
            print("no user")
            return redirect(url_for("signup.signup"))
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for("home.home"))
        else:
            flash("Invalid Password")
            return render_template("login.html")

    elif request.method == "GET":
        return render_template("login.html")


@login_blueprint.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.home"))
