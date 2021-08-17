from flask import Blueprint, request, json
from flask_restful import Resource, Api

from app.models import Article
from app.serializer.article_schema import ArticleSchema, article_list

article_bp = Blueprint('articles', __name__, url_prefix='/article')
api = Api(article_bp)

class Articles(Resource):
    def get(self):
        articles = Article.query.order_by(Article.created.desc()).all()

        return article_list.dump(articles)

class ArticleApi(Resource):
    def post(self):
        from marshmallow import ValidationError
        try:
            article_request = ArticleSchema().loads(request.data)
        except ValidationError as error:
            return error.messages, 422

        try:
            article = Article(
                title=article_request['title'],
                abstract=article_request['abstract'],
                content=article_request['content'],
                user_id=article_request['user_id'],
                category_id=article_request['category_id']
            )
        except Exception as sql_error:
            return sql_error.args, 401

        return {
            'msg': 'Artigo não cadastrado',
            'status': 401
        }

api.add_resource(Articles, '/', '/all/', endpoint='all')