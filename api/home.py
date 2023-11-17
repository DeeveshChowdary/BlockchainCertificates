from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user

home_blueprint = Blueprint("home", __name__, template_folder="templates")


@home_blueprint.route("/")
def home():
    return render_template("home.html")
