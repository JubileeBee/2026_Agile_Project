import os

# Base directory of the application (used to build DB path)
basedir = os.path.abspath(os.path.dirname(__file__))

# Default SQLite database location if no environment variable is set
default_db_path = 'sqlite:///' + os.path.join(basedir, 'cozycravings.db')

class Config:
    # Database configuration (supports environment variable override for deployment)
    SQLALCHEMY_DATABASE_URI = os.environ.get('COZYCRAVINGS_DATABASE_URL') or default_db_path

    # Secret key used for sessions, cookies, and security features
    SECRET_KEY = os.environ.get('COZYCRAVINGS_SECRET_KEY') or 'dev-secret-key'