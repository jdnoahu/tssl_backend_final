from flask import Blueprint, request, jsonify
from src.models import MemberSchema, Member
from src.common import db


member_bp = Blueprint("member_bp", __name__)

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)


# Endpoint to create a new member
@member_bp.route('/api/member', methods=["POST"])
def add_member():
    first_name = request.json['member']['first_name']
    last_name = request.json['member']['last_name']
    sobriety_date = request.json['member']['sobriety_date']
    email = request.json['member']['email']
    password = request.json['member']['password']

    new_member = Member(first_name, last_name, sobriety_date, email, password)

    db.session.add(new_member)
    db.session.commit()

    member = Member.query.get(new_member.id)

    return member_schema.jsonify(member)


# endpoint all members
@member_bp.route("/api/members", methods=["GET"])
def get_members():
    all_members = Member.query.all()
    result = members_schema.dump(all_members)
    return jsonify(result)


# endpoint single member
@member_bp.route("/api/member/<id>", methods=["GET"])
def get_member(id):
    member = Member.query.get(id)
    return member_schema.jsonify(member)


# Update edit member
@member_bp.route("/api/member/<id>", methods=["PUT"])
def member_update(id):
    member = Member.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    sobriety_date = request.json['sobriety_date']
    email = request.json['email']
    password = request.json['password']

    member.first_name = first_name
    member.last_name = last_name
    member.sobriety_date = sobriety_date
    member.email = email
    member.password = password

    db.session.commit()
    return member_schema.jsonify(member)


# Endpoint delete Record
@member_bp.route("/api/member/<id>", methods=["DELETE"])
def member_delete(id):
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()

    return "member was deleted"
