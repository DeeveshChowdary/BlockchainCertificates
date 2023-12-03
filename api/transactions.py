from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_required, current_user
from constants.web3 import getWeb3

transactions_blueprint = Blueprint(
    "transactions", __name__, template_folder="templates"
)
from services.transaction_service import (
    send_transaction,
    get_transaction_details,
    get_all_transactions,
)
from flask import jsonify
from models.users import User


@transactions_blueprint.route("/make_transaction", methods=["POST"])
def send_eth_transaction():
    sender_address = request.form.get("sender_address", None)
    sender_private_key = request.form.get("sender_private_key", None)
    recipient_address = request.form.get("recipient_address", None)
    value = 0
    data = request.form.get("data", None)

    if not (sender_address and sender_private_key and recipient_address and data):
        return jsonify({"message": "Incomplete Data"})

    tx_hash = send_transaction(
        sender_address, sender_private_key, recipient_address, value, data
    )

    return jsonify({"tx_hash": tx_hash})


@transactions_blueprint.route("/get_transaction_information", methods=["GET"])
def get_transaction_information():
    transaction_hash = request.form.get("transaction_hash", None)

    if not transaction_hash:
        transaction_hash = request.args.get("transaction_hash", None)

    if not transaction_hash:
        return jsonify({"message": "Incomplete Data"})

    data = get_transaction_details(transaction_hash)

    return jsonify({"Message": data})


@transactions_blueprint.route("/issue_certificate", methods=["GET", "POST"])
@login_required
def issue_certificate():
    if request.method == "GET":
        issue_user_id = request.args.get("user_id")
        issue_user = User.query.get(issue_user_id)
        return render_template(
            "issue_certificate.html", current_user=current_user, issue_user=issue_user
        )
    else:
        sender_address = request.form.get("sender_address", None)
        sender_private_key = request.form.get("sender_private_key", None)
        recipient_address = request.form.get("recipient_address", None)

        data = {}

        if request.form.get("certificate_type") == "Education":
            data["Transaction Type"] = "Education"
            data["Grade"] = request.form.get("grade")
            data["University"] = request.form.get("university")
            data["School"] = request.form.get("school")
        else:
            data["Transaction Type"] = "Experience"
            data["role"] = request.form.get("role")
            data["company"] = request.form.get("company")
            data["comments"] = request.form.get("comments")

        tx_hash = send_transaction(
            sender_address, sender_private_key, recipient_address, 0, data
        )

        return render_template("home.html")


@transactions_blueprint.route("/get_public_id_transactions", methods=["GET"])
def get_public_id_transactions():
    public_id = request.args.get("public_id", None)

    if public_id is None:
        return []

    tx_list = get_all_transactions(public_id)

    return jsonify({"transaction hashes": tx_list})
