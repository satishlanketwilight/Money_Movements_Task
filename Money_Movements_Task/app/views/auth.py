import datetime

from flask import jsonify, make_response, render_template, request, url_for
from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_smorest import abort, Blueprint
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.users import UserModel

from flask_login import login_user, logout_user, login_required, \
    current_user
from app.schemas.users import UserSchema, UserSingleOutputSchema, UserListOutputSchema
from app.services.users import UserService
from app.exceptions.users import UserObjectNotFound

auth_blp = Blueprint('auth', __name__, url_prefix='/auth',
                     description='All operations for an Authentication')


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
        username = request.form['username']
        password = request.form['password']
        user = UserModel.query.filter_by(username=username).first()
        if user:
            authenticated = check_password_hash(user.password, password)
            print(authenticated)
        if not authenticated:
            return redirect(url_for('auth.Login'))
        # print(user.user_id)
        # print(user)
        
        login_user(user,remember=True)
        return redirect(url_for('movements.MovementsList'))


@auth_blp.route('/register')
class Register(MethodView):
    """Api view class for single User object operations"""

    @staticmethod
    def get():
        """ Render the Login Page.
        """
        return make_response(render_template('register.html', ))
