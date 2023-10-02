from config import Config
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

# MongoDB Configuration
mongo_client = MongoClient(Config.MONGO_URI, server_api=ServerApi('1'))
db = mongo_client.get_database("blog_db")
posts_collection = db.get_collection("posts")

#TODO: Fix Creat New Post. Doesn't work because it's expecting an _id and isn't finding one
class Post:
    def __init__(self, _id, title, content, author, date, tags):
        self._id = _id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.tags = tags

    def save(self):
        result = posts_collection.insert_one(self.__dict__)
        self._id = result.inserted_id

    @classmethod
    def find_by_id(cls, post_id):
        # Find a post by its _id
        post_data = posts_collection.find_one({"_id": ObjectId(post_id)})
        if post_data:
            return cls(**post_data)
        return None
    
    @classmethod
    def find_all(cls):
        # Find all posts
        posts_data = posts_collection.find({})
        return [cls(**post) for post in posts_data]
    
    def update(self):
        # Update a post
        posts_collection.update_one({"_id": self._id}, {"$set": self.__dict__})

    def delete(self):
        # Delte a post from the collection
        posts_collection.delete_one({"_id": self._id})
