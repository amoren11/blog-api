from flask import Blueprint, jsonify, request
from app.services import post_service

# Create a Bluprint for the blog posts
posts_bp = Blueprint("posts", __name__, url_prefix="/api/posts")

# Create a new blog post
@posts_bp.route("/", methods=["POST"])
def create_new_post():
    data = request.get_json()
    post = post_service.create_post(data)
    post["_id"] = str(post["_id"])
    return jsonify(post), 201

# Get all blog posts
@posts_bp.route("/", methods=["GET"])
def get_all_posts():
    posts = post_service.get_posts()
    # ObjectId not JSON Serializable
    for post in posts:
        post["_id"] = str(post["_id"])
    return jsonify(posts)

# Get a specific blog post by its ID
@posts_bp.route("/<string:post_id>", methods=["GET"])
def get_post(post_id):
    post = post_service.get_post_by_id(post_id)
    if post:
        post["_id"] = str(post["_id"])
        return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

# Update a specific blog post by its ID
@posts_bp.route("/<string:post_id>", methods=["PUT"])
def update_existing_post(post_id):
    data = request.get_json()
    
    updated_post = post_service.update_post(post_id, data)
    if updated_post:
        updated_post["_id"] = str(updated_post["_id"])
        return jsonify(updated_post)
    return jsonify({"error": "Post not found or no changes were made"}), 404

# Delete a specific blog post by its ID
@posts_bp.route("/<string:post_id>", methods=["DELETE"])
def delete_post(post_id):
    result = post_service.delete_post(post_id)
    if not result:
        return jsonify({"error": "Post not found"})
    return jsonify({"message": "Successfully deleted post!"})
