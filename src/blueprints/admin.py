from flask import Blueprint, request, jsonify
from src.models import AdminSchema, Admin
from src.common import db


admin_bp = Blueprint("admin_bp", __name__)

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)


# Endpoint to create a new admin
@admin_bp.route('/api/admin', methods=["POST"])
def add_admin():
    email = request.json['admin']['email']
    password = request.json['admin']['password']

    new_admin = Admin(email, password)

    db.session.add(new_admin)
    db.session.commit()

    admin = Admin.query.get(new_admin.id)

    return admin_schema.jsonify(admin)


# endpoint all admins
@admin_bp.route("/api/admins", methods=["GET"])
def get_admins():
    all_admins = Admin.query.all()
    result = admins_schema.dump(all_admins)
    return jsonify(result)


# endpoint single admin
@admin_bp.route("/api/admin/<id>", methods=["GET"])
def get_admin(id):
    admin = Admin.query.get(id)
    return admin_schema.jsonify(admin)


# Update edit admin
@admin_bp.route("/api/admin/<id>", methods=["PUT"])
def admin_update(id):
    admin = Admin.query.get(id)
    email = request.json['email']
    password = request.json['password']

    admin.email = email
    admin.password = password

    db.session.commit()
    return admin_schema.jsonify(admin)


# Endpoint delete Record
@admin_bp.route("/api/admin/<id>", methods=["DELETE"])
def admin_delete(id):
    admin = Admin.query.get(id)
    db.session.delete(admin)
    db.session.commit()

    return "admin was deleted"
