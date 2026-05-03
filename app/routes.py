from flask import render_template
from app import app
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    recipe = Recipe.query.get_or_404(id)
    return render_template('recipe.html', recipe=recipe)