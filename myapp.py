from app import app, db

# Create database tables if they don't already exist
# (only runs when the app starts directly)
from app.models import Recipe

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)