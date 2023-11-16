try:
    from __main__ import db
except ImportError:
    from app import db

from sqlalchemy import JSON


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    profile_information = db.Column(JSON)

    def __init__(self, kwargs={}):
        profile_information = {}
