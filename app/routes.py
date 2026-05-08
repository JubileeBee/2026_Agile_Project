from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Recipe
from sqlalchemy import desc, func
from app.models import Recipe, CategoryEnum, Like
import random

# Helper functions: This can be added to other pages if you want to implement it
def get_random_by_category(category, limit=10):
    """Get random recipes by category"""
    if category is None:
        return []
    recipes = Recipe.query.filter(Recipe.category == category).all()
    random.shuffle(recipes)
    return recipes[:limit]


def get_trending_recipes(limit=10):
    """Get top recipes by most likes"""
    results = (
        db.session.query(
            Recipe,
            func.count(Like.id).label("like_count")
        )
        .outerjoin(Like, Recipe.id == Like.recipe_id)
        .group_by(Recipe.id)
        .order_by(func.count(Like.id).desc())
        .limit(limit)
        .all()
    )
    # extract just the Recipe objects from the tuples
    return [recipe for recipe, like_count in results]


def get_recent_recipes(limit=10):
    """Get most recently added recipes, shuffled"""
    recipes = Recipe.query.order_by(desc(Recipe.created_at)).limit(limit).all()
    random.shuffle(recipes)
    return recipes


def get_quick_meals(limit=10):
    """Get recipes with cook time under 30 mins, shuffled"""
    recipes = (
        Recipe.query
        .filter(Recipe.cook_time != None)
        .filter(Recipe.cook_time <= 30)
        .order_by(desc(Recipe.created_at))
        .limit(limit)
        .all()
    )
    random.shuffle(recipes)
    return recipes

@app.route('/')
def home():
    try:
        trending_recipes = get_trending_recipes(limit=10)
        recent_recipes = get_recent_recipes(limit=10)
        quick_meals = get_quick_meals(limit=10)
        dinner_recipes = get_random_by_category(CategoryEnum.DINNER, limit=10)
        dessert_recipes = get_random_by_category(CategoryEnum.DESSERT, limit=10)

        sections = [
            {"title": "This Week's Comfort Obsessions", "recipes": trending_recipes, "class": "top-6-section"},
            {"title": "Recently Added", "recipes": recent_recipes, "class": "recent-history"},
            {"title": "Quick Meals (Under 30 mins)", "recipes": quick_meals, "class": ""},
            {"title": "Dinner Ideas", "recipes": dinner_recipes, "class": ""},
            {"title": "Desserts", "recipes": dessert_recipes, "class": ""},
        ]

        total_recipes = Recipe.query.count()

        return render_template('index.html',
                             sections=sections,
                             total_recipes=total_recipes,
                             error=None)

    except Exception as e:
        print("Database Error:", e)
        return render_template('index.html',
                             sections=[],
                             total_recipes=0,
                             error=None)

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
def privacy():
    return render_template("privacy.html")


@app.route("/terms_and_condition")
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
            {
                'id': 1,
                'title': 'Chocolate Lava Cake',
                'category': 'Dessert',
                'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400',
                'rating': 4.8,
                'likes': 231,
                'duration': '30 mins'
            },
            {
                'id': 6,
                'title': 'Banana Pancakes',
                'category': 'Breakfast',
                'image_url': 'https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg',
                'rating': 4.9,
                'likes': 278,
                'duration': '20 mins'
            },
        ],
        'favourites': [
            {
                'id': 4,
                'title': 'Caesar Salad',
                'category': 'Lunch',
                'image_url': 'https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg',
                'rating': 4.3,
                'likes': 98,
                'duration': '15 mins'
            },
        ],
        'likes': [
            {
                'id': 3,
                'title': 'Soy Sauce Ramen',
                'category': 'Dinner',
                'image_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s',
                'rating': 4.7,
                'likes': 312,
                'duration': '45 mins',
                'profile': 'Mia Chen'
            },
        ]
    }

    return render_template('profile.html', user=user)


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

    related_recipes = Recipe.query.filter(
        Recipe.id != recipe.id
    ).limit(4).all()

    return render_template(
        'recipe.html',
        recipe=recipe,
        related_recipes=related_recipes
    )

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

# Vanessa's route added by Nabeel

@app.route('/api/recipes')
def api_recipes():
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '', type=str)
    category = request.args.get('category', '', type=str)

    query = Recipe.query

    # Search filter
    if search:
        query = query.filter(Recipe.title.ilike(f'%{search}%'))

    # Category filter
    if category:
        query = query.filter(Recipe.category == category)

    per_page = 6

    pagination = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    recipes_data = []

    for recipe in pagination.items:
        recipes_data.append({
            'id': recipe.id,
            'title': recipe.title,
            'image_url': getattr(recipe, 'image_url', ''),
            'likes': getattr(recipe, 'likes_count', 0),
            'rating': getattr(recipe, 'rating', 0)
        })

    return jsonify({
        'recipes': recipes_data,
        'has_more': pagination.has_next
    })