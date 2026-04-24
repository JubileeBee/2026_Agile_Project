# Main Flask application handling server-side routing and rendering of Jinja2 templates.
# The @app.route decorators map specific URLs to the functions that render the HTML pages.

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    test_recipe = {
        'id': 1,
        'title': 'Chocolate Lava Brownie C...',
        'category': 'Dessert',
        'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400',
        'rating': 4.8,
        'likes': 231,
        'duration': '30 mins',
        'profile': 'Emma Doe'
    }

    return render_template(
        'index.html',
        trending_recipes=[test_recipe],
        recent_recipes=[],
        recommended_recipes=[]
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