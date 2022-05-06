from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

api = Api()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
