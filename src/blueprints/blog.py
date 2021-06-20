from flask import Blueprint, request, jsonify
from src.models import BlogSchema, Blog
from src.common import db


blog_bp = Blueprint("blog_bp", __name__)

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)


# Endpoint to create a new blog
@blog_bp.route('/api/blog', methods=["POST"])
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
@blog_bp.route("/api/blogs", methods=["GET"])
def get_blogs():
    all_blogs = Blog.query.all()
    result = blogs_schema.dump(all_blogs)
    return jsonify(result)


# endpoint single blog
@blog_bp.route("/api/blogs/<id>", methods=["GET"])
def get_blog(id):
    blog = Blog.query.get(id)
    return blog_schema.jsonify(blog)


# Update edit blog
@blog_bp.route("/api/blog/<id>", methods=["PUT"])
def blog_update(id):
    blog = Blog.query.get(id)
    title = request.json['title']
    category = request.json['category']
    featured_image = request.json['featured_image']
    content = request.json['content']
    tags = request.json['tags']

    blog.title = title
    blog.category = category
    blog.featured_image = featured_image
    blog.content = content
    blog.tags = tags

    db.session.commit()
    return blog_schema.jsonify(blog)


# Endpoint delete Record
@blog_bp.route("/api/blog/<id>", methods=["DELETE"])
def blog_delete(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()

    return "blog was deleted"
