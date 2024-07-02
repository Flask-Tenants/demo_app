from flask import g, jsonify


def tenant_index():
    tenant = g.tenant if hasattr(g, 'tenant') else 'unknown'
    return jsonify({"message": f"Welcome to the tenant index page for {tenant}!"}), 200
