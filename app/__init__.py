from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():      
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login-view = "auth.login"

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify ({
        "error": "Too Many Requests",
        "message": "You have exceeded your rate limit. Please try again later."
    }), 429

#register blueprints

from app.auth import auth_bp
from app.main import main_bp

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

return app

from app import routes, models

from flask import Blueprint
from flask import Blueprint

auth_bp = Blueprint("auth", __name__)
