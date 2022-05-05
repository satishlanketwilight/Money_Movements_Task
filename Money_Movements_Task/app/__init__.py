from flask import Flask

from flask_login import LoginManager 
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from app.common import api, db, migrate,login
        api.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)
        
        login.init_app(app)
        login.login_view = 'auth.Login'
        app.secret_key = "caaaee521afa236c6796cc4a7368b1a993b0e1b712065161ca696e0eb93069ad"

        from app.views.movements import movement_blp, movements_blp
        api.register_blueprint(movement_blp)
        api.register_blueprint(movements_blp)

        from app.views.users import user_blp, users_blp

        api.register_blueprint(user_blp)
        api.register_blueprint(users_blp)

        from app.views.auth import auth_blp

        api.register_blueprint(auth_blp)

        return app
