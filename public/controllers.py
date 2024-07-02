import logging
from flask import g, jsonify, request
from .models import Tenant, Domain
from sqlalchemy import text

logging.basicConfig(level=logging.DEBUG)


def public_index():
    return 'Welcome to the public index page!'


def deactivate_tenant(tenant_name):
    try:
        tenant = g.db_session.query(Tenant).get(tenant_name)
        if not tenant:
            return jsonify({'error': 'Tenant not found'}), 404
        tenant.deactivated = True
        g.db_session.commit()
        return jsonify({'message': f'Tenant {tenant.name} deactivated successfully'}), 200
    except Exception as e:
        g.db_session.rollback()
        return jsonify({'error': str(e)}), 500


def activate_tenant(tenant_name):
    tenant_name = tenant_name.lower()
    try:
        tenant = g.db_session.query(Tenant).filter_by(name=tenant_name).first()
        if not tenant:
            return jsonify({'error': 'Tenant not found'}), 404
        tenant.deactivated = False
        g.db_session.commit()
        return jsonify({'message': f'Tenant {tenant.name} activated successfully'}), 200
    except Exception as e:
        g.db_session.rollback()
        return jsonify({'error': str(e)}), 500


def create_tenant_route():
    data = request.json
    logging.debug("create_tenant_route called")
    logging.debug(f"Request data: {data}")

    if not data:
        return jsonify({"error": "Invalid input data"}), 400

    tenant_data = {k: v for k, v in data.items() if k in Tenant.__table__.columns.keys()}
    domain_name = data.get('domain_name')
    if not domain_name:
        return jsonify({"error": "domain_name is required"}), 400

    existing_tenant = Tenant.query.filter_by(name=tenant_data['name']).first()
    if existing_tenant:
        return jsonify({"error": f"Tenant with name {tenant_data['name']} already exists"}), 400

    tenant = Tenant(**tenant_data)
    try:
        print(g.db_session.execute(text("show search_path")).fetchone())
        g.db_session.add(tenant)
        print(1)
        g.db_session.flush()  # Flush to get the tenant ID
        print(2)
        logging.debug(f"Tenant {tenant.name} added to session")

        domain = Domain(domain_name=domain_name, tenant_id=tenant.id, is_primary=True, tenant_name=tenant.name)
        g.db_session.add(domain)
        print(3)
        g.db_session.commit()
        print(4)
        logging.debug(f"Domain {domain_name} for tenant {tenant.name} added and committed")

        return jsonify({"message": f"Tenant {tenant.name} created successfully", "tenant": {
            "id": tenant.id,
            "name": tenant.name,
            "phone_number": tenant.phone_number,
            "address": tenant.address,
            "domain_name": domain_name
        }}), 201
    except Exception as e:
        g.db_session.rollback()
        logging.error(f"Error creating tenant: {e}")
        return jsonify({"error": str(e)}), 500


def get_tenant_route(tenant_name):
    try:
        tenant = g.db_session.query(Tenant).filter_by(name=tenant_name).first()
        if not tenant:
            return jsonify({"error": "Tenant not found"}), 404
        return jsonify({
            "id": tenant.id,
            "name": tenant.name,
            "phone_number": tenant.phone_number,
            "address": tenant.address
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def update_tenant_route(tenant_name):
    tenant_name = tenant_name.lower()
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input data"}), 400

    try:
        tenant = g.db_session.query(Tenant).filter_by(name=tenant_name).first()
        if not tenant:
            return jsonify({"error": "Tenant not found"}), 404

        new_name = data.get('name')
        if new_name and new_name != tenant_name:
            old_tenant_name = tenant.name
            tenant.name = new_name
            g.db_session.commit()  # Commit tenant update first

            # Only change the tenant name reference in the domain, but do not change domain values
            domain = g.db_session.query(Domain).filter_by(tenant_name=old_tenant_name).first()
            if domain:
                domain.tenant_name = new_name
                g.db_session.commit()

        for key, value in data.items():
            if key in Tenant.__table__.columns.keys() and key != 'name':
                setattr(tenant, key, value)

        g.db_session.commit()  # Commit tenant update
        return jsonify({
            "message": f"Tenant {tenant.name} updated successfully",
            "tenant": {
                "name": tenant.name,
                "phone_number": tenant.phone_number,
                "address": tenant.address
            }
        }), 200
    except Exception as e:
        g.db_session.rollback()
        return jsonify({"error": str(e)}), 500


def delete_tenant_route(tenant_name):
    tenant_name = tenant_name.lower()
    try:
        tenant = g.db_session.query(Tenant).filter_by(name=tenant_name).first()
        if not tenant:
            logging.error(f"Tenant {tenant_name} not found")
            return jsonify({"error": "Tenant not found"}), 404

        logging.debug(f"Deleting tenant: {tenant.name}")

        g.db_session.query(Domain).filter_by(tenant_name=tenant_name).delete()

        g.db_session.delete(tenant)
        g.db_session.commit()

        logging.debug(f"Successfully deleted tenant and its domains: {tenant.name}")

        return jsonify({"message": "Tenant and its schema deleted successfully"}), 200
    except Exception as e:
        g.db_session.rollback()
        logging.error(f"Error deleting tenant: {e}")
        return jsonify({"error": str(e)}), 500


def deactivate_tenant_route(tenant_name):
    tenant_name = tenant_name.lower()
    try:
        tenant = g.db_session.query(Tenant).filter_by(name=tenant_name).first()
        if not tenant:
            return jsonify({'error': 'Tenant not found'}), 404
        tenant.deactivated = True
        g.db_session.commit()
        return jsonify({'message': f'Tenant {tenant.name} deactivated successfully'}), 200
    except Exception as e:
        g.db_session.rollback()
        return jsonify({'error': str(e)}), 500


def activate_tenant_route(tenant_name):
    tenant_name = tenant_name.lower()
    try:
        tenant = g.db_session.query(Tenant).filter_by(name=tenant_name).first()
        if not tenant:
            return jsonify({'error': 'Tenant not found'}), 404
        tenant.deactivated = False
        g.db_session.commit()
        return jsonify({'message': f'Tenant {tenant.name} activated successfully'}), 200
    except Exception as e:
        g.db_session.rollback()
        return jsonify({'error': str(e)}), 500
