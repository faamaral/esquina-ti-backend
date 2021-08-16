from flask_admin import Admin

from app.models import db
from app.models import User
from app.admin.user_admin import UserAdmin
from app.routes.admin_view import IndexView

admin = Admin()

def init_app(app):

    admin.name = 'Esquina da TI Administração'
    admin.template_mode = 'bootstrap4'
    admin.index_view = IndexView()
    admin.add_view(UserAdmin(User, db.session))

    admin.init_app(app)