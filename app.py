from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from flask_cors import CORS
from datetime import datetime
from flask import request, render_template

app = Flask(__name__)
CORS(app, supports_credentials=True)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)


db = SQLAlchemy(app)
ma = Marshmallow(app)

'sqlite:///' + \
    os.path.join(basedir, 'app.sqlite')


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(144), unique=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password


class AdminSchema(ma.Schema):
    class Meta:
        fields = ('email', 'password')


admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)

# Endpoint to create a new admin


@app.route('/admin', methods=["POST"])
def add_admin():
    email = request.json['admin']['email']
    password = request.json['admin']['password']

    new_admin = Admin(email, password)

    db.session.add(new_admin)
    db.session.commit()

    admin = Admin.query.get(new_admin.id)

    return admin_schema.jsonify(admin)

# endpoint all admins


@app.route("/admins", methods=["GET"])
def get_admins():
    all_admins = Admin.query.all()
    result = admins_schema.dump(all_admins)
    return jsonify(result)


# endpoint single admin

@app.route("/admin/<id>", methods=["GET"])
def get_admin(id):
    admin = Admin.query.get(id)
    return admin_schema.jsonify(admin)

# Update edit admin


@app.route("/admin/<id>", methods=["PUT"])
def admin_update(id):
    admin = Admin.query.get(id)
    email = request.json['email']
    password = request.json['password']

    admin.email = email
    admin.password = password

    db.session.commit()
    return admin_schema.jsonify(admin)

# Endpoint delete Record


@app.route("/admin/<id>", methods=["DELETE"])
def admin_delete(id):
    admin = Admin.query.get(id)
    db.session.delete(admin)
    db.session.commit()

    return "admin was deleted"


# MEMBER DATABASE
class Member(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False)
    last_name = db.Column(db.String(100), unique=False)
    sobriety_date = db.Column(db.String(100), unique=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(144), unique=False)

    def __init__(self, first_name, last_name, sobriety_date, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.sobriety_date = sobriety_date
        self.email = email
        self.password = password


class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name',
                  'sobriety_date', 'email', 'password')

# class MemberImages(db.Model):
 #   member_id


member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

# Endpoint to create a new member


@app.route('/member', methods=["POST"])
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


@app.route("/members", methods=["GET"])
def get_members():
    all_members = Member.query.all()
    result = members_schema.dump(all_members)
    return jsonify(result)


# endpoint single member

@app.route("/member/<id>", methods=["GET"])
def get_member(id):
    member = Member.query.get(id)
    return member_schema.jsonify(member)

# Update edit member


@app.route("/member/<id>", methods=["PUT"])
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


@app.route("/member/<id>", methods=["DELETE"])
def member_delete(id):
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()

    return "member was deleted"

# BLOG DATABASE


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    category = db.Column(db.String(100), unique=False)
    creation_date = db.Column(db.String(100), unique=False)
    featured_image = db.Column(db.String(100), unique=False)
    content = db.Column(db.Text(), unique=False)
    tags = db.Column(db.String(144), unique=False)

    def __init__(self, title, category, creation_date, featured_image, content, tags):
        self.title = title
        self.category = category
        self.creation_date = creation_date
        self.featured_image = featured_image
        self.content = content
        self.tags = tags


class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id','title', 'category', 'creation_date',
                  'featured_image', 'content', 'tags')


blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)

# Endpoint to create a new blog


@app.route('/blog', methods=["POST"])
def add_blog():

    title = request.json['title']
    category = request.json['category']
    creation_date = request.json['creation_date']
    featured_image = request.json['featured_image']
    content = request.json['content']
    tags = request.json['tags']

    new_blog = Blog(title, category, creation_date,
                    featured_image, content, tags)

    db.session.add(new_blog)
    db.session.commit()

    blog = Blog.query.get(new_blog.id)

    return blog_schema.jsonify(blog)

# endpoint all blogs


@app.route("/blogs", methods=["GET"])
def get_blogs():
    all_blogs = Blog.query.all()
    result = blogs_schema.dump(all_blogs)
    return jsonify(result)


# endpoint single blog

@app.route("/blogs/<id>", methods=["GET"])
def get_blog(id):
    blog = Blog.query.get(id)
    return blog_schema.jsonify(blog)

# Update edit blog


@app.route("/blog/<id>", methods=["PUT"])
def blog_update(id):
    blog = Blog.query.get(id)
    title = request.json['title']
    category = request.json['category']
    # creation_date = request.json['creation_date']
    featured_image = request.json['featured_image']
    content = request.json['content']
    tags = request.json['tags']

    blog.title = title
    blog.category = category
    # blog.creation_date = creation_date
    blog.featured_image = featured_image
    blog.content = content
    blog.tags = tags

    db.session.commit()
    return blog_schema.jsonify(blog)

# Endpoint delete Record


@app.route("/blog/<id>", methods=["DELETE"])
def blog_delete(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()

    return "blog was deleted"


if __name__ == '__main__':
    app.run(debug=True)
