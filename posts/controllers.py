from flask import request, jsonify, abort, g
from .models import Post


def create_post_route():
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    author = data.get('author')

    if not title or not body or not author:
        abort(400, description="Post name and capacity are required")

    post = Post(title=title, body=body, author=author)
    g.db_session.add(post)
    g.db_session.commit()
    return jsonify({"message": "Post created successfully"}), 201


def get_posts_route():
    posts = g.db_session.query(Post).all()
    post_list = [{"id": post.id, "title": post.title, "body": post.body, "author": post.author} for post in
                 posts]
    return jsonify(post_list), 200


def update_post_route(post_id):
    post = g.db_session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404, description="Post not found")

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.body = data.get('body', post.body)
    post.author = data.get('author', post.author)

    g.db_session.commit()
    return jsonify({"message": "Post updated successfully"}), 200


def delete_post_route(post_id):
    post = g.db_session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404, description="Post not found")

    g.db_session.delete(post)
    g.db_session.commit()
    return jsonify({"message": "Post deleted successfully"}), 200
