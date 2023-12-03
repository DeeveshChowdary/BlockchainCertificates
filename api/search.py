from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from models.users import User
from services.search_service import perform_search

search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/search", methods=["GET"])
def search():

    query = request.args.get("query", None)

    print(query)
    if query:
        response = perform_search(query)
        return render_template("search_results.html", results=response)
    else:
        return render_template("home.html")
