from flask import render_template, request, redirect, url_for
from app import app, limiter, db
from app.models import Recipe

@app.route('/')
def home():
    recipes = Recipe.query.all()
    return render_template(
        'index.html',
        trending_recipes=recipes,
        recent_recipes=recipes[1:5] if len(recipes) > 1 else [],
        recommended_recipes=recipes
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

@app.route("/privacy_policy")
@limiter.exempt  # Exempt privacy policy from rate limiting to ensure accessibility
def privacy():
    return render_template("privacy.html")

@app.route("/terms_and_condition")
@limiter.exempt  # Exempt terms and conditions from rate limiting to ensure accessibility
def terms():
    return render_template("terms.html")

@app.route('/profile')
def profile():
    user = {
        'name': 'Emma Doe',
        'bio': 'This is where the bio goes.',
        'recipes_count': 12,
        'likes_count': 48,
        'favourites_count': 23,
        'is_owner': True,
        'recipes': [
            {'id': 1, 'title': 'Chocolate Lava Cake', 'category': 'Dessert', 'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400', 'rating': 4.8, 'likes': 231, 'duration': '30 mins'},
            {'id': 6, 'title': 'Banana Pancakes', 'category': 'Breakfast', 'image_url': 'https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg', 'rating': 4.9, 'likes': 278, 'duration': '20 mins'},
        ],
        'favourites': [
            {'id': 4, 'title': 'Caesar Salad', 'category': 'Lunch', 'image_url': 'https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg', 'rating': 4.3, 'likes': 98, 'duration': '15 mins'},
        ],
        'likes': [
            {'id': 3, 'title': 'Soy Sauce Ramen', 'category': 'Dinner', 'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s', 'rating': 4.7, 'likes': 312, 'duration': '45 mins', 'profile': 'Mia Chen'},
        ]
    }
    return render_template('profile.html', user=user)

@app.route('/signup')
# Apply rate limit to the signup route for anti-spam and abuse prevention
@limiter.limit("3 per minute")
def signup():
    return render_template('signup.html')

@app.route('/login')
# Apply rate limit to the login route to prevent brute force attacks
@limiter.limit("5 per minute")
def login():
    return render_template('login.html')

@app.route('/post')
# Apply rate limit to the post route to prevent spam
@limiter.limit("10 per hour")
def post():
    return render_template('post.html')

@app.route('/recipe/<int:id>')
@limiter.limit("60 per minute")  # Limit recipe detail views to prevent scraping
def recipe_detail(id):
    recipe = Recipe.query.get_or_404(id)
    return render_template('recipe.html', recipe=recipe)

@app.route('/edit_recipe/<int:id>', methods=['GET', 'POST'])
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)

    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        recipe.category = request.form['category']
        recipe.image_url = request.form['image_url']

        db.session.commit()
        return redirect(url_for('recipe_detail', id=recipe.id))

    return render_template('edit_recipe.html', recipe=recipe)