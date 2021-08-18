from flask import Blueprint
from flask_restful import Resource, Api

from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.models import Article, db, User
from app.serializer.user_schema import ListUserSchema

author_bp = Blueprint('author_bp', __name__, url_prefix='/author')
api = Api(author_bp)

class ListAuthor(Resource):

    def get(self, id):
        try:
            user_schema = ListUserSchema()
            user = User.query.filter_by(id=id).first_or_404(description=f'Usuário com id = {id} não encontrado')
            return user_schema.dump(user)
        except SQLAlchemyError as err:
            return err.args, 501
        return {
            'msg': 'Não foi possivel obter o autor',
            'status': 501
        }, 501

class ListAuthors(Resource):
    def get(self):
        try:
            user_schema = ListUserSchema(many=True)
            users = User.query.order_by(User.id.desc()).all()
            return user_schema.dump(users), 201
        except SQLAlchemyError as err:
            return err.args, 501
        return {
                   'msg': 'Não foi possivel obter o autor',
                   'status': 501
               }, 501


api.add_resource(ListAuthor, '/<int:id>')
api.add_resource(ListAuthors, '/')