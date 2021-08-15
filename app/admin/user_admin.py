import uuid
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash


class UserAdmin(ModelView):
    form_excluded_columns = ['reset_password']

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)
        model.reset_password = uuid.uuid4()