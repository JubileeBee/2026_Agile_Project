from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(300), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    likes = db.Column(db.Integer, default=0)
    duration = db.Column(db.String(50), nullable=True)
    profile = db.Column(db.String(100), nullable=True)

def create_test_data():
    recipes = [
        Recipe(title='Chocolate Lava Cake', category='Dessert', image_url='https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400', rating=4.8, likes=231, duration='30 mins', profile='Emma Doe'),
        Recipe(title='Avocado Toast', category='Breakfast', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPfqIDCCdL5IDo0IOwcXdOx6q8o7V6su_lCg&s', rating=4.5, likes=189, duration='10 mins', profile='Jake Lee'),
        Recipe(title='Soy Sauce Ramen', category='Dinner', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s', rating=4.7, likes=312, duration='45 mins', profile='Mia Chen'),
        Recipe(title='Caesar Salad', category='Lunch', image_url='https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg', rating=4.3, likes=98, duration='15 mins', profile='Tom Hill'),
        Recipe(title='Mango Smoothie', category='Drinks', image_url='https://twosleevers.com/wp-content/uploads/2025/05/Mango-Smoothie-1.jpg', rating=4.6, likes=145, duration='5 mins', profile='Sara Kim'),
        Recipe(title='Banana Pancakes', category='Breakfast', image_url='https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg', rating=4.9, likes=278, duration='20 mins', profile='Chris Ray'),
    ]
    db.session.add_all(recipes)
    db.session.commit()