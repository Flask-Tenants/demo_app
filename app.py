from flask import Flask
from flask_migrate import Migrate
from flask_tenants import FlaskTenants
from config import Config
from public.routes import public_bp
from tenants.routes import tenant_bp
from posts.routes import post_bp
from errors import register_error_handlers
from public.models import Tenant, Domain
from flask_tenants import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register error handlers
    register_error_handlers(app)

    # Initialize tenants app
    flask_tenants = FlaskTenants(app, tenant_model=Tenant, domain_model=Domain, db=db, tenant_url_prefix='/_tenant')
    flask_tenants.init()

    # Initialize Flask-Migrate
    Migrate(app, db)

    # Create tenancy middleware
    root_public_bp = flask_tenants.create_public_blueprint('public')
    root_tenant_bp = flask_tenants.create_tenant_blueprint('tenant')
    root_post_bp = flask_tenants.create_tenant_blueprint('post')

    # Register blueprints
    root_public_bp.register_blueprint(public_bp)
    root_tenant_bp.register_blueprint(tenant_bp)
    root_post_bp.register_blueprint(post_bp)

    app.register_blueprint(root_public_bp)
    app.register_blueprint(root_tenant_bp)
    app.register_blueprint(root_post_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
