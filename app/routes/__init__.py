from app.routes.auth import auth
from app.routes.admin_view import auth_admin
from app.routes.articles import article_bp

def init_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(auth_admin)
    app.register_blueprint(article_bp)