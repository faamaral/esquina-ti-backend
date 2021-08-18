from app.serializer import ma
from marshmallow import fields

from app.models import User

class UserSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class RegisterSchema(ma.Schema):
    full_name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

class ListUserSchema(ma.Schema):
    id = fields.Integer(required=True)
    full_name = fields.Str()
    username = fields.Str()
    email = fields.Email()





