from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman

# Create Flask app globally
app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)  # Enable CSRF protection
Talisman(app)  # Enable security headers

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

# Import routes and models LAST
from app import routes, models