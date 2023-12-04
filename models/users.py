try:
    from __main__ import db
except ImportError:
    from app import db

from models.profiles import Profile

from flask_login import UserMixin, login_manager


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(100))
    public_key = db.Column(db.String(100), unique=True)
    profile_id = db.Column(
        db.Integer, db.ForeignKey(Profile.id, ondelete="CASCADE"), nullable=False
    )
    profile = db.relationship("Profile", backref=db.backref("users", lazy="dynamic"))

    def __init__(self, kwargs):
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")
        self.role = kwargs.get("role")

    @classmethod
    def getAll(cls):
        return User.query.all()

    def __repr__(self) -> str:
        return "{}, {}".format(self.first_name, self.last_name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
