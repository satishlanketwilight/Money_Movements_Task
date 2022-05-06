import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.common import db, login


class AuthModel(UserMixin, db.Model):
    """Auth model class made for storing objects in database"""
    __tablename__ = 'auth'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(length=80), unique=True)
    email = db.Column(db.String(length=100), unique=True)
    password = db.Column(db.String(200))
    date_joined = db.Column(db.Date, default=datetime.datetime.today)

    def set_password(self, password):
        """Create hashed password"""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password"""
        return check_password_hash(self.password, password)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'User : {self.email} : {self.username}'


@login.user_loader
def load_user(user):
    return AuthModel.query.get(user)
