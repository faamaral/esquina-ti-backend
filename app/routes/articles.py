import datetime
from slugify import slugify

from flask import Blueprint, request, json
from flask_restful import Resource, Api
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.models import Article, db
from app.serializer.article_schema import ArticleSchema, article_list, article_get_one, ArticleListSchema

article_bp = Blueprint('articles', __name__, url_prefix='/article')
api = Api(article_bp)

class Articles(Resource):
    def get(self):
        try:
            articles = Article.query.order_by(Article.created.desc()).all()
        except Exception as exc:
            return exc.args

        return article_list.dump(articles)
    def post(self):

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
            db.session.add(article)
            db.session.commit()
            return {
                'msg': 'Artigo cadastrado com sucesso!',
                'status': 201
            }, 201
        except Exception as sql_error:
            return sql_error.args, 401

        return {
            'msg': 'Artigo não cadastrado',
            'status': 401
        }



class ArticleApi(Resource):
    def get(self, id):
        try:
            artic = Article.query.filter_by(id=id).one()
            response = ArticleListSchema().dump(artic)
            return response, 201

        except Exception as exc:
            return exc.args
        return {
            'msg': 'artigo não encontrado',
            'status': 500
        }, 500

    def put(self, id):
        try:
            article_request = article_get_one.loads(request.data)
        except ValidationError as error:
            return error.messages, 422
        try:
            article = Article.query.filter_by(id=id).one()
            if 'title' in article_request:
                article.title = article_request['title']
                article.slug = slugify(article.title.__str__())
            if 'abstract' in article_request:
                article.abstract=article_request['abstract']
            if 'content' in article_request:
                article.content=article_request['content']
            if 'category_id' in article_request:
                article.category_id=article_request['category_id']
            article.last_edit = datetime.datetime.utcnow()

            db.session.add(article)
            db.session.commit()
            return {
                       'msg': 'Artigo atualizado com sucesso!',
                       'status': 201
                   }, 201
        except SQLAlchemyError as exc:
            return exc.args
        return {
            'msg': 'Não foi possivel cadastrar',
            'status': 501
        }, 501
    def delete(self):
        try:
            article = Article.query.filter_by(id=id).first_or_404(description=f'ID={id} não foi encontrado')

            db.session.delete(article)
            db.session.commit()
            return {
                       'msg': 'Artigo excluido com sucesso!',
                       'status': 201
                   }, 201
        except SQLAlchemyError as exc:
            return exc.args
        return {
            'msg': f'Não foi possivel excluir o artigo com ID = {id}',
            'status': 501
        }, 501





api.add_resource(Articles, '/', '/all/', endpoint='all')
api.add_resource(ArticleApi, '/<int:id>', '/<int:id>/')