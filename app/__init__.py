from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bootstrap import Bootstrap
from flask_adminlte3 import AdminLTE3

from config import Development, Production
from .models import db
from app.serializer import ma
from app import admin
from app import routes
from app import login

migrate = Migrate()
jwt = JWTManager()
def create_app(config_class=Production):
    app = Flask(__name__)
    app.config.from_object(config_class)
    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    AdminLTE3(app)
    routes.init_app(app)
    return app
    