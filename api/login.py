from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user
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

        print("EMAIL", email)
        print("Password", password)
        user = User.query.filter(User.email == email).first()
        dummy = User.query.all()
        print("All data", dummy)
        print("User: ", user)
        if not user:
            print("no user")
            return redirect(url_for("signup.signup"))
        if check_password_hash(user.password, password):
            # login_user(user, remember=remember)
            return redirect(url_for("home.home"))

        else:
            flash("Invalid Password")
            return

    elif request.method == "GET":
        return render_template("login.html")
