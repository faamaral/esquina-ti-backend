from app.serializer import ma

from marshmallow import fields

class ArticleSchema(ma.Schema):
    title = fields.Str(required=True)
    abstract = fields.Str(required=True)
    content = fields.Str(required=True)
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)

class ArticleListSchema(ma.Schema):
    id = fields.Integer(required=True)
    title = fields.Str(required=True)
    abstract = fields.Str(required=True)
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
    created = fields.DateTime(required=True)
    last_edit = fields.DateTime(required=True)

article_list = ArticleListSchema(many=True)