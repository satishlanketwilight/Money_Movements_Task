from flask import jsonify, make_response, render_template, request
from flask.views import MethodView
from flask_smorest import abort, Blueprint

from app.schemas.users import UserSchema, UserSingleOutputSchema, UserListOutputSchema
from app.services.users import UserService
from app.exceptions.users import UserObjectNotFound

user_blp = Blueprint('user', __name__, url_prefix='/users',
                     description='All operations for a single user object')
users_blp = Blueprint('users', __name__, url_prefix='/users',
                      description='All operations for a list of user objects')

user_service = UserService()

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_blp.route('/<user_id>')
class User(MethodView):
    """Api view class for single User object operations"""

    @staticmethod
    @user_blp.response(200, UserSingleOutputSchema)
    def get(user_id):
        """Read a single user
        Return single user object.
        """
        try:
            user = user_service.get_by_id(user_id)
            user_json = user_schema.dump(user)
            # return jsonify({'user': user_json}), 200
            return make_response(render_template('movements.html', data=user_json))
        except UserObjectNotFound:
            abort(404, message='User not found.')


@users_blp.route('/')
class UsersList(MethodView):
    """Api view class for a list of User objects operations"""

    @staticmethod
    @users_blp.response(200, UserListOutputSchema)
    def get():
        """Read all users
        Return all user objects.
        """
        users = user_service.get_all()
        users_json = users_schema.dump(users)

        # return jsonify({'users': users_json}), 200
        return make_response(render_template('movements.html', data=users_json))

    @staticmethod
    # @users_blp.arguments(UserSchema)
    @users_blp.response(201, UserSingleOutputSchema)
    def post():
        """Create a new user
        Add a new user object.
        """
        user_data = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        }
        user = user_service.create(user_data)
        user_json = user_schema.dump(user)
        return jsonify({'user': user_json}), 201
