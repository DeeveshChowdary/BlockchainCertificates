from flask_login import current_user
from models.users import User
from database import db


def update_profile_service(data):

    print(current_user)

    user = User.query.get(current_user.id)
    user.first_name = (
        data.get("first_name")
        if data.get("first_name", None) is not None
        else user.first_name
    )
    user.last_name = (
        data.get("last_name")
        if data.get("last_name", None) is not None
        else user.last_name
    )
    user.public_key = (
        data.get("public_key")
        if data.get("public_key", None) is not None
        else user.public_key
    )
    db.session.commit()
    return
