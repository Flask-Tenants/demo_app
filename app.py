from flask import Flask
from flask_migrate import Migrate
from flask_tenants import init_app as tenants_init_app, create_tenancy, db
from config import Config
from public.models import Tenant, Domain
from public.routes import public_bp
from tenants.routes import tenant_bp
from posts.routes import post_bp
import logging


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize tenants app
    tenants_init_app(app, tenant_model=Tenant, domain_model=Domain)

    # Initialize Flask-Migrate
    Migrate(app, db)

    # Create tenancy middleware
    tenancy_middleware = create_tenancy(app, db=db, tenant_url_prefix='/_tenant')

    root_public_bp = tenancy_middleware.create_public_blueprint('public')
    root_tenant_bp = tenancy_middleware.create_tenant_blueprint('tenant')
    root_post_bp = tenancy_middleware.create_tenant_blueprint('post')

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
