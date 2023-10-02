from flask import Flask
from flask_cors import CORS
from app.routes.posts import posts_bp

app = Flask(__name__)

# Enable CORS
CORS(app)

# Register Blueprints for different routes
app.register_blueprint(posts_bp)

#TODO: Authentication Later? 👀
# app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()