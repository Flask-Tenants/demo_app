from flask_tenants import BaseTenant, BaseDomain, db


class Tenant(BaseTenant):
    __tablename__ = 'tenants'
    phone_number = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    deactivated = db.Column(db.Boolean, nullable=False, default=False)


class Domain(BaseDomain):
    __tablename__ = 'domains'
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    tenant_name = db.Column(db.String(128), nullable=False)
    domain_name = db.Column(db.String(255), unique=True, nullable=False)
    is_primary = db.Column(db.Boolean, default=False, nullable=False)
