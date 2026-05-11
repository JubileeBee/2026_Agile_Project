import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Use environment variable ONLY (no hardcoded fallback)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQLite database path
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False