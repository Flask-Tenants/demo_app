from flask import request, jsonify, abort
from .models import Post
from flask_tenants.utils import with_db


def create_post_route():
    with with_db() as session:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        body = data.get('body')

        if not title or not body or not author:
            abort(400, description="Post title, body, and author are required")

        post = Post(title=title, author=author, body=body)
        session.add(post)
        session.commit()
        return jsonify({"message": "Post created successfully"}), 201


def get_posts_route():
    with with_db() as session:
        posts = session.query(Post).all()
        post_list = [{"id": post.id, "title": post.title, "author": post.author, "body": post.body} for post
                     in
                     posts]
        return jsonify(post_list), 200


def update_post_route(post_id):
    with with_db() as session:
        post = session.query(Post).filter_by(id=post_id).first()
        if not post:
            abort(404, description="Post not found")

        data = request.get_json()
        post.title = data.get('title', post.title)
        post.author = data.get('author', post.author)
        post.body = data.get('body', post.body)

        session.commit()
        return jsonify({"message": "Post updated successfully"}), 200


def delete_post_route(post_id):
    with with_db() as session:
        post = session.query(Post).filter_by(id=post_id).first()
        if not post:
            abort(404, description="Post not found")

        session.delete(post)
        session.commit()
        return jsonify({"message": "Post deleted successfully"}), 200
