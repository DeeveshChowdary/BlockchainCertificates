from flask import Blueprint, request, redirect, url_for, render_template
from sqlalchemy import exc
from werkzeug.security import generate_password_hash
from database import db
from models.users import User
from models.profiles import Profile

signup_blueprint = Blueprint("signup", __name__, template_folder="templates")


@signup_blueprint.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":
        data = {
            "first_name": request.form.get("first_name", None),
            "last_name": request.form.get("last_name", None),
            "email": request.form.get("email", None),
            "password": generate_password_hash(
                request.form.get("password", None), method="sha256"
            ),
        }

        profile = Profile()
        try:
            db.session.add(profile)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
        user = User(data)
        user.profile_id = profile.id
        user.profile = profile
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("login.login"))
        except exc.SQLAlchemyError as e:
            db.session.rollback()
        return render_template("signup.html")
    elif request.method == "GET":
        return render_template("signup.html")
