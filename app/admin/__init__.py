from flask_admin import Admin, AdminIndexView, expose

from app.models import db
from app.models import User, Category, Article
from app.admin.user_admin import UserAdmin
from app.admin.articles_admin import ArticleAdmin
from app.admin.category_admin import CategoryAdmin


admin = Admin()

def init_app(app):

    admin.name = 'Esquina da TI Administração'
    admin.template_mode = 'bootstrap3'
    #admin.index_view = MyAdminIndexView()
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(CategoryAdmin(Category, db.session))
    admin.add_view(ArticleAdmin(Article, db.session))

    admin.init_app(app)