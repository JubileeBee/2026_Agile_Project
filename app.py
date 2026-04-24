# Main Flask application handling server-side routing and rendering of Jinja2 templates.
# The @app.route decorators map specific URLs to the functions that render the HTML pages.

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    test_recipes = [
        {'id': 1, 'title': 'Chocolate Lava Cake', 'category': 'Dessert', 'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400', 'rating': 4.8, 'likes': 231, 'duration': '30 mins', 'profile': 'Emma Doe'},
        {'id': 2, 'title': 'Avocado Toast', 'category': 'Breakfast', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPfqIDCCdL5IDo0IOwcXdOx6q8o7V6su_lCg&s', 'rating': 4.5, 'likes': 189, 'duration': '10 mins', 'profile': 'Jake Lee'},
        {'id': 3, 'title': 'Soy Sauce Ramen', 'category': 'Dinner', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s', 'rating': 4.7, 'likes': 312, 'duration': '45 mins', 'profile': 'Mia Chen'},
        {'id': 4, 'title': 'Caesar Salad', 'category': 'Lunch', 'image_url': 'https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg', 'rating': 4.3, 'likes': 98, 'duration': '15 mins', 'profile': 'Tom Hill'},
        {'id': 5, 'title': 'Mango Smoothie', 'category': 'Drinks', 'image_url': 'https://twosleevers.com/wp-content/uploads/2025/05/Mango-Smoothie-1.jpg', 'rating': 4.6, 'likes': 145, 'duration': '5 mins', 'profile': 'Sara Kim'},
        {'id': 6, 'title': 'Banana Pancakes', 'category': 'Breakfast', 'image_url': 'https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg', 'rating': 4.9, 'likes': 278, 'duration': '20 mins', 'profile': 'Chris Ray'},
    ]

    return render_template('index.html',
        trending_recipes=test_recipes,
        recent_recipes=test_recipes[:4],
        recommended_recipes=test_recipes
    )

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/post')
def post():
    return render_template('post.html')

# Route for displaying a single recipe detail page
# The <int:id> allows dynamic URLs like /recipe/1, /recipe/2

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    return render_template('recipe.html', recipe_id=id)

if __name__ == '__main__':
    app.run(debug=True)