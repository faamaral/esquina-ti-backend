from flask import Blueprint, request, json
from flask_restful import Resource, Api
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.models import Category
from app.serializer.category_schema import category_get_one, category_list

category_bp = Blueprint('categories', __name__, url_prefix='/category')
api = Api(category_bp)

class ListCategory(Resource):
    def get(self):
        try:
            categories = Category.query.order_by(Category.id.desc()).all()
            return category_list.dump(categories), 201
        except SQLAlchemyError as err:
            return err.args, 501
        return {
            'msg': 'Erro ao buscar as categorias',
            'status': 401
        }

class GetCategory(Resource):
    def get(self, id):
        try:
            category = Category.query.filter_by(id=id).all()
            return category_get_one.dump(category), 201
        except SQLAlchemyError as err:
            return err.args, 501
        return {
            'msg': 'Categoria não encontrada',
            'status': 401
        }

api.add_resource(ListCategory, '/')
api.add_resource(GetCategory, '/<int:id>', '/<int:id>/')