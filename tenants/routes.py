from flask import Blueprint
from .controllers import (
    tenant_index
)

tenant_bp = Blueprint('tenant', __name__)


@tenant_bp.route('/')
def index():
    return tenant_index()
