from api.login import login_blueprint
from api.signup import signup_blueprint
from api.home import home_blueprint
from api.transactions import transactions_blueprint
from api.search import search_blueprint
from api.manage_user_details import user_details_blueprint
from api.profile import profile_blueprint


class RegisterBlueprints:
    def __init__(self, app, db):
        app.register_blueprint(login_blueprint)
        app.register_blueprint(signup_blueprint)
        app.register_blueprint(home_blueprint)
        app.register_blueprint(transactions_blueprint)
        app.register_blueprint(search_blueprint)
        app.register_blueprint(user_details_blueprint)
        app.register_blueprint(profile_blueprint)
        # pass
