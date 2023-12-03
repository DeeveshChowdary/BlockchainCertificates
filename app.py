import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS
from flask_migrate import Migrate

from database import db
from initializers.register_all_blueprints import RegisterBlueprints
from initializers.setup_config import SetupConfig

# from initializers.engine import engine
from sqlalchemy import create_engine

from flask_login import LoginManager

from models.users import User

app = Flask(__name__)

with app.app_context():
    SetupConfig(app)
    db.init_app(app)

    migration = Migrate(app, db, directory="migrations", compare_type=True)

    cors = CORS(app)
    RegisterBlueprints(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    port = int(os.environ.get("PORT", 8000))

    app.run(host="0.0.0.0", port=port)
