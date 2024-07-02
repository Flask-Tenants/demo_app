from flask import Blueprint
from public.controllers import (
    create_tenant_route,
    get_tenant_route,
    update_tenant_route,
    delete_tenant_route,
    deactivate_tenant_route,
    activate_tenant_route
)

public_bp = Blueprint('public', __name__)


@public_bp.route('/')
def index():
    return 'Welcome to the public index page!'


@public_bp.route('/create_tenant', methods=['POST'])
def create_tenant():
    return create_tenant_route()


@public_bp.route('/get_tenant/<tenant_name>', methods=['GET'])
def get_tenant(tenant_name):
    return get_tenant_route(tenant_name)


@public_bp.route('/update_tenant/<tenant_name>', methods=['PUT'])
def update_tenant(tenant_name):
    return update_tenant_route(tenant_name)


@public_bp.route('/delete_tenant/<tenant_name>', methods=['DELETE'])
def delete_tenant(tenant_name):
    return delete_tenant_route(tenant_name)


@public_bp.route('/deactivate_tenant/<tenant_name>', methods=['PUT'])
def deactivate_tenant(tenant_name):
    return deactivate_tenant_route(tenant_name)


@public_bp.route('/activate_tenant/<tenant_name>', methods=['PUT'])
def activate_tenant(tenant_name):
    return activate_tenant_route(tenant_name)

