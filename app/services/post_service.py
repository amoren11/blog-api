from app.models.post import Post
from bson import ObjectId
from datetime import datetime

def create_post(data):
    """
    Create a new blog post.

    Args: 
        data (dict): Data for the new blog post.

    Returns:
        dict: Newly created blog post
    """
    post = Post(
        _id=ObjectId(),
        title=data.get("title"),
        content=data.get("content"),
        author=data.get("author"),
        date=datetime.now(),
        tags=data.get("tags")
    )
    post.save()
    return post.__dict__

def get_posts():
    """
    Get all blog posts

    Returns:
        list: List of all blog posts
    """
    posts = Post.find_all()
    return [post.__dict__ for post in posts]

def get_post_by_id(post_id):
    """
    Get a specific blog post by ID

    Args:
        post_id (str): ID of the blog post to find

    Returns:
        dict: Blog post
    """
    post = Post.find_by_id(post_id)
    if post:
        return post.__dict__
    return None

def update_post(post_id, data):
    """
    Update a blog post

    Args:
        post_id (str): ID of the blog post being updated
        data (dict): Updated data for the blog post

    Returns:
    1   dict: Updated blog post data
    """
    post = Post.find_by_id(post_id)
    if post:
        # Update the post
        for key, value in data.items():
            setattr(post, key, value)
        post.update()
        return post.__dict__
    return None

def delete_post(post_id):
    """
    Delete a blog post

    Args:
        post_id (str): ID of the blog post to be deleted

    Returns:
        dict: Deleted blog post data
    """
    post = Post.find_by_id(post_id)
    if post:
        post.delete()
        return post.__dict__
    return None
