from app.models import Article
from app.serializer import ma

from marshmallow import fields

class ArticleSchema(ma.Schema):
    title = fields.Str(required=True)
    abstract = fields.Str(required=True)
    content = fields.Str(required=True)
    user_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)

class ArticleListSchema(ma.Schema):
    class Meta:
        model = Article
        include_fk = True
    id = fields.Integer(required=True)
    title = fields.Str()
    abstract = fields.Str()
    slug = fields.Str()
    content = fields.Str()
    user_id = fields.Integer()
    category_id = ma.Function(lambda obj: obj.category.name)
    created = fields.DateTime()
    last_edit = fields.DateTime()

article_list = ArticleListSchema(many=True)
article_get_one = ArticleListSchema()