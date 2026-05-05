from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# Set up rate limiting with Flask-Limiter
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per hour", "50 per minute"]
)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify ({
        "error": "Too Many Requests",
        "message": "You have exceeded your rate limit. Please try again later."
    }), 429

from app import routes, models