from app.serializer import ma

from marshmallow import fields

class CategorySchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)


category_list = CategorySchema(many=True)
category_get_one = CategorySchema()