# Main Flask application handling server-side routing and rendering of Jinja2 templates.
# The @app.route decorators map specific URLs to the functions that render the HTML pages.

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    test_recipes = [
        {'id': 1, 'title': 'Chocolate Lava Cake', 'category': 'Dessert', 'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400', 'rating': 4.8, 'likes': 231, 'duration': '30 mins', 'profile': 'Emma Doe', 'ingredients': 'Chocolate, Eggs, Butter'},
        {'id': 2, 'title': 'Avocado Toast', 'category': 'Breakfast', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPfqIDCCdL5IDo0IOwcXdOx6q8o7V6su_lCg&s', 'rating': 4.5, 'likes': 189, 'duration': '10 mins', 'profile': 'Jake Lee', 'ingredients': 'Avocado, Bread'},
        {'id': 3, 'title': 'Soy Sauce Ramen', 'category': 'Dinner', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s', 'rating': 4.7, 'likes': 312, 'duration': '45 mins', 'profile': 'Mia Chen', 'ingredients': 'Ramen Noodle, Water, Soy Sauce'},
        {'id': 4, 'title': 'Caesar Salad', 'category': 'Lunch', 'image_url': 'https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg', 'rating': 4.3, 'likes': 98, 'duration': '15 mins', 'profile': 'Tom Hill', 'ingredients': 'Lettuce, Egg, Bacon, Chicken, Ceasar Sauce'},
        {'id': 5, 'title': 'Mango Smoothie', 'category': 'Drinks', 'image_url': 'https://twosleevers.com/wp-content/uploads/2025/05/Mango-Smoothie-1.jpg', 'rating': 4.6, 'likes': 145, 'duration': '5 mins', 'profile': 'Sara Kim', 'ingredients': 'Mango, Water, Ice'},
        {'id': 6, 'title': 'Banana Pancakes', 'category': 'Breakfast', 'image_url': 'https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg', 'rating': 4.9, 'likes': 278, 'duration': '20 mins', 'profile': 'Chris Ray', 'ingredients': 'Banana, Eggs, Flour, Sugar, Water, Milk'},
    ]

    return render_template('index.html',
        trending_recipes=test_recipes,
        recent_recipes=test_recipes[1:5],
        recommended_recipes=test_recipes
    )
@app.route("/recipes")
def recipes():
    return render_template("browse_recipes.html")

@app.route("/favourites")
def favourites():
    return render_template("favourites.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/contact")
def contact():
    return render_template("contact_us.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/privacy_policy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms_and_condition")
def terms():
    return render_template("terms.html")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/post')
def post():
    return render_template('create_recipe_page.html')

# Route for displaying a single recipe detail page
# The <int:id> allows dynamic URLs like /recipe/1, /recipe/2

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    return render_template('recipe.html', recipe_id=id)

#if __name__ == '__main__':
#    app.run(debug=True)

@app.route('/login')
def login():
    return render_template('login.html')


# Edit Recipe Page, App Code, notably rendering our data outside of home function there.

def get_all_recipes():
    return [
        {'id': 1, 'title': 'Chocolate Lava Cake', 'category': 'Dessert', 'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400', 'rating': 4.8, 'likes': 231, 'duration': '30 mins', 'profile': 'Emma Doe', 'ingredients': 'Chocolate, Eggs, Butter'},
        {'id': 2, 'title': 'Avocado Toast', 'category': 'Breakfast', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPfqIDCCdL5IDo0IOwcXdOx6q8o7V6su_lCg&s', 'rating': 4.5, 'likes': 189, 'duration': '10 mins', 'profile': 'Jake Lee', 'ingredients': 'Avocado, Bread'},
        {'id': 3, 'title': 'Soy Sauce Ramen', 'category': 'Dinner', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s', 'rating': 4.7, 'likes': 312, 'duration': '45 mins', 'profile': 'Mia Chen', 'ingredients': 'Ramen Noodle, Water, Soy Sauce'},
        {'id': 4, 'title': 'Caesar Salad', 'category': 'Lunch', 'image_url': 'https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg', 'rating': 4.3, 'likes': 98, 'duration': '15 mins', 'profile': 'Tom Hill', 'ingredients': 'Lettuce, Egg, Bacon, Chicken, Ceasar Sauce'},
        {'id': 5, 'title': 'Mango Smoothie', 'category': 'Drinks', 'image_url': 'https://twosleevers.com/wp-content/uploads/2025/05/Mango-Smoothie-1.jpg', 'rating': 4.6, 'likes': 145, 'duration': '5 mins', 'profile': 'Sara Kim', 'ingredients': 'Mango, Water, Ice'},
        {'id': 6, 'title': 'Banana Pancakes', 'category': 'Breakfast', 'image_url': 'https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg', 'rating': 4.9, 'likes': 278, 'duration': '20 mins', 'profile': 'Chris Ray', 'ingredients': 'Banana, Eggs, Flour, Sugar, Water, Milk'},
    ]

def get_recipe_by_id(recipe_id):
    recipes = get_all_recipes()
    return next((r for r in recipes if r['id'] == recipe_id), None)

@app.route('/edit_recipe/<int:recipe_id>')
def edit_recipe_page(recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    return render_template('edit_recipe_page.html', recipe=recipe)

@app.route('/edit_recipe/<int:recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    recipe = get_recipe_by_id(recipe_id)

    if recipe:
        recipe['title'] = request.form['title']
        recipe['ingredients'] = request.form['ingredients']

    return redirect(url_for('recipe_detail', id=recipe_id))

# Create_recipe python code:
@app.route('/create_recipe')
def create_recipe_page():
    return render_template('create_recipe_page.html')

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    title = request.form['title']
    ingredients = request.form['ingredients']
    steps = request.form['steps']

    # For now, just print (since no DB)
    print("New Recipe:", title, ingredients, steps)

    return redirect(url_for('home'))

app.run(debug=True)