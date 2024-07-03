from flask import jsonify
from flask_tenants.exceptions import TenantNotFoundError, TenantActivationError


def register_error_handlers(app):
    @app.errorhandler(TenantNotFoundError)
    def handle_tenant_not_found(error):
        response = jsonify({
            'error': 'TenantNotFoundError',
            'message': 'The requested tenant was not found.'
        })
        response.status_code = 404
        return response

    @app.errorhandler(TenantActivationError)
    def handle_tenant_activation_error(error):
        response = jsonify({
            'error': 'TenantActivationError',
            'message': 'The requested tenant is deactivated.'
        })
        response.status_code = 403
        return response
