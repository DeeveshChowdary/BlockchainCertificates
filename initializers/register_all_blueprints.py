from api.login import login_blueprint
from api.signup import signup_blueprint
from api.home import home_blueprint
from api.transactions import transactions_blueprint


class RegisterBlueprints:
    def __init__(self, app, db):
        app.register_blueprint(login_blueprint)
        app.register_blueprint(signup_blueprint)
        app.register_blueprint(home_blueprint)
        app.register_blueprint(transactions_blueprint)
        # pass
