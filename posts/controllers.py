from flask import request, jsonify, abort, g
from .models import Post


def create_post_route():
    data = request.get_json()
    name = data.get('name')
    capacity = data.get('capacity')
    location = data.get('location')

    if not name or not capacity:
        abort(400, description="Post name and capacity are required")

    post = Post(name=name, capacity=capacity, location=location)
    g.db_session.add(post)
    g.db_session.commit()
    return jsonify({"message": "Post created successfully"}), 201


def get_posts_route():
    posts = g.db_session.query(Post).all()
    post_list = [{"id": post.id, "name": post.name, "capacity": post.capacity, "location": post.location} for post in
                 posts]
    return jsonify(post_list), 200


def update_post_route(post_id):
    post = g.db_session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404, description="Post not found")

    data = request.get_json()
    post.name = data.get('name', post.name)
    post.capacity = data.get('capacity', post.capacity)
    post.location = data.get('location', post.location)

    g.db_session.commit()
    return jsonify({"message": "Post updated successfully"}), 200


def delete_post_route(post_id):
    post = g.db_session.query(Post).filter_by(id=post_id).first()
    if not post:
        abort(404, description="Post not found")

    g.db_session.delete(post)
    g.db_session.commit()
    return jsonify({"message": "Post deleted successfully"}), 200
