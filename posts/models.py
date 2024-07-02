from flask_tenants.models import db, BaseTenantModel


class Post(BaseTenantModel):
    __abstract__ = False
    __tablename__ = 'posts'
    __table_args__ = {'info': {'tenant_specific': True}}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=True)
    body = db.Column(db.String(10000), nullable=True)
    author = db.Column(db.String(255), nullable=True)
