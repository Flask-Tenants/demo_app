from flask import Blueprint
from posts.controllers import (
    create_post_route,
    get_posts_route,
    update_post_route,
    delete_post_route
)

post_bp = Blueprint('post_bp', __name__, url_prefix='/posts')


@post_bp.route('', methods=['POST'])
def create_post():
    return create_post_route()


@post_bp.route('', methods=['GET'])
def get_posts():
    return get_posts_route()


@post_bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    return update_post_route(post_id)


@post_bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    return delete_post_route(post_id)
