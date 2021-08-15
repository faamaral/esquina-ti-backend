from app.serializer import ma

from marshmallow import fields

class ArticleSchema(ma.Schema):
    title = fields.Str(required=True)
    abstract = fields.Str(required=True)
    content = fields.Str(required=True)
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)