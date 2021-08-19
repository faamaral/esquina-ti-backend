from app.routes.auth import auth
from app.routes.admin_view import auth_admin
from app.routes.articles import article_bp
from app.routes.author import author_bp
from app.routes.categories import category_bp

def init_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(auth_admin)
    app.register_blueprint(article_bp)
    app.register_blueprint(author_bp)
    app.register_blueprint(category_bp)