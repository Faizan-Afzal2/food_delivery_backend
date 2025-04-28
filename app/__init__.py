# app/__init__.py
from flask import Flask
from app.routes.order_routes import bp as order_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(order_bp, url_prefix="/api")
    return app
