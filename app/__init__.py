from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_wtf.csrf import CSRFProtect
import secrets

# Create Flask app globally
app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = secrets.token_hex(32)  # Generate a random secret key
csrf = CSRFProtect(app)  # Enable CSRF protection

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

# Import routes and models LAST
from app import routes, models