from flask import Blueprint, request, redirect, url_for, render_template, flash, jsonify
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash

from models.users import User
from services.search_service import perform_search
from services.profile_service import update_profile_service


user_details_blueprint = Blueprint(
    "user_details", __name__, template_folder="templates"
)


@user_details_blueprint.route("/update_profile", methods=["POST", "GET"])
@login_required
def update_profile():
    if request.method == "GET":
        return render_template("manage_user_details.html", user=current_user)
    else:

        data = {
            "first_name": request.form.get("first_name", None),
            "last_name": request.form.get("last_name", None),
            "public_key": request.form.get("public_key", None),
        }

        update_profile_service(data)

        return render_template("manage_user_details.html", user=current_user)
