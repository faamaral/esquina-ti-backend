import datetime
import json

from flask import Blueprint, request
from flask_restful import Resource, Api
from app.serializer.user_schema import UserSchema, RegisterSchema
from app.models import User, db
from flask_jwt_extended import create_access_token, create_refresh_token
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from flask_login import current_user, login_user, logout_user

auth = Blueprint('auth', __name__, url_prefix='/auth')
auth_api = Api(auth)

class Login(Resource):
    def post(self):

        try:
            usern = UserSchema().loads(request.data)
        except ValidationError as error:
            return error.messages, 422

        user = User.query.filter_by(username=usern['username']).first()
        if user and user.verify_password(request.json['password']):
            access_token = create_access_token(
                identity=user.id,
                expires_delta=datetime.datetime.now() + datetime.timedelta(days=5)
            )
            refresh_token = create_refresh_token(identity=user.id)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'status': 201
            }
        return {
            'msg': 'Usuário ou senha incorretos',
            'status': 401
        }

class Register(Resource):
    def post(self):

        try:
            usern = RegisterSchema().loads(request.data)
        except ValidationError as error:
            return error.messages, 422

        try:
            user = User(full_name=usern['full_name'], username=usern['username'], email=usern['email'], password=usern['password'])
            db.session.add(user)
            db.session.commit()
            access_token = create_access_token(
                identity=user.id,
                expires_delta=datetime.timedelta(days=5)
            )
            refresh_token = create_refresh_token(identity=user.id)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'status': 201
            }
        except Exception as sql_error:
            return sql_error.code, 400
        return {
            'msg': 'Usuário ou senha incorretos',
            'status': 401
        }


auth_api.add_resource(Login, '/login/', endpoint="login")
auth_api.add_resource(Register, '/register/', endpoint='register')