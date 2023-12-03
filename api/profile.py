from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash

from models.users import User
from services.search_service import perform_search

from services.transaction_service import get_all_transactions

profile_blueprint = Blueprint("profile", __name__, template_folder="templates")


@profile_blueprint.route("/view_profile", methods=["GET"])
def view_profile():

    id = request.args.get("id", None)

    user = User.query.get(int(id))

    print("USER ID", user.id)
    print("PUBLIC KEY", user.public_key)

    certificates = get_all_transactions(user.public_key)

    return render_template("view_profile.html", user=user, current_user=current_user, certificates=certificates)


@profile_blueprint.route("/view_my_profile", methods=["GET"])
@login_required
def view_my_profile():
    user = current_user

    certificates = get_all_transactions(user.public_key)

    return render_template("view_profile.html", user=user, current_user=current_user, certificates=certificates)
