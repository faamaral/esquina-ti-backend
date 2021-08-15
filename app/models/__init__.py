import uuid
from datetime import datetime

import slugify as slugify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from app.login import login

db = SQLAlchemy()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    full_name = Column('full_name', String(50), nullable=False)
    username = Column('username', String(20), nullable=False, unique=True, index=True)
    email = Column('email', String(35), nullable=False, unique=True, index=True)
    password = Column('password', String, nullable=False)
    reset_password = Column('reset_password', String, nullable=False, unique=True)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, full_name, username, email, password, admin=False):
        self.full_name = full_name,
        self.username = username,
        self.email = email,
        self.password = generate_password_hash(password)
        self.reset_password = uuid.uuid4()
        self.admin = admin

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'admin': self.admin
        }

    def __repr__(self) -> str:
        return f'<User> -> {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), index=True, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Category> -> {self.name}'

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)

    user_id = db.Column('author', db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)

    abstract = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_edit = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    category_id = db.Column('category',db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', foreign_keys=category_id)

    def __init__(self, title, user_id, abstract, content, category_id):
        self.title=title
        self.slug = slugify(title)
        self.user_id=user_id
        self.abstract=abstract
        self.content=content
        self.category_id=category_id

