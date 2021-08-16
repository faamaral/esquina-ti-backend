import uuid
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash
from flask_login import current_user
from flask import session
from app.models import User


class UserAdmin(ModelView):
    form_excluded_columns = ['reset_password']
    column_list = ['id', 'full_name', 'username', 'email', 'admin']

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)
        model.reset_password = uuid.uuid4()

    def is_accessible(self):

        if current_user.is_authenticated:

            user = User.query.get(current_user.id)
            if user.admin:
                return True
        return False