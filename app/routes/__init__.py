from app.routes.auth import auth
from app.routes.admin_view import auth_admin

def init_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(auth_admin)