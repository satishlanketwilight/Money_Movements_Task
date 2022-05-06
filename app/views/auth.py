import flask_login
from flask import make_response, render_template, request, url_for
from flask.views import MethodView
from flask_smorest import Blueprint
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash
from app.models.users import AuthModel
from app.logs import logger
from flask_login import login_user, current_user

auth_blp = Blueprint('auth', __name__, url_prefix='/auth',
                     description='All operations for an Authentication')


@auth_blp.route('/logout')
class Logout(MethodView):
    @staticmethod
    def get():
        """ logout the user
        """
        flask_login.logout_user()
        return make_response(render_template('index.html'))


@auth_blp.route('/login')
class Login(MethodView):
    """Api view class for single User object operations"""

    @staticmethod
    def get():
        """ Render the Login Page.
        """
        if current_user.is_authenticated:
            return redirect(url_for('movements.MovementsList'))

        return make_response(render_template('index.html', ))

    @staticmethod
    def post():
        """ Login process with username and password params
        """
        authenticated = False
        username = request.form['username']
        password = request.form['password']
        user = AuthModel.query.filter_by(username=username).first()
        if user:
            authenticated = check_password_hash(user.password, password)
        if not authenticated:
            logger.info(f"{username} attempted to login")
            return redirect(url_for('auth.Login'))

        login_user(user, remember=True)
        return redirect(url_for('movements.MovementsList'))


@auth_blp.route('/register')
class Register(MethodView):
    """Api view class for single User object operations"""

    @staticmethod
    def get():
        """ Render the Login Page.
        """
        return make_response(render_template('register.html', ))
