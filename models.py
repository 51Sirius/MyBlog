from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255), nullable=True)
    score = db.Column(db.Integer, default=0)
    class_user = db.Column(db.Integer, default=5)
    level = db.Column(db.Integer, default=1)
    last_answer = db.Column(db.String, default=None)
    snake = db.Column(db.Integer, default=0)
    tetris = db.Column(db.Integer, default=0)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)