from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config  # keep root config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

# Redirect unauthenticated users to login
login.login_view = 'login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Rate limiting (Ivy's addition)
    limiter = Limiter(
        key_func=get_remote_address,
        app=app,
        default_limits=["200 per hour", "50 per minute"]
    )

    @app.errorhandler(429)
    def ratelimit_handler(e):
        return jsonify({
            "error": "Too Many Requests",
            "message": "You have exceeded your rate limit. Please try again later."
        }), 429

    # Import routes and models
    from app import routes, models

    return app