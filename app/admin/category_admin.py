from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.models import User

class CategoryAdmin(ModelView):

    def is_accessible(self):
        if current_user.is_authenticated:
            user = User.query.get(current_user.id)
            if user.admin:
                return True
        return False