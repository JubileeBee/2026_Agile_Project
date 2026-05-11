from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from sqlalchemy import desc, func
from flask_login import login_user, login_required, current_user, logout_user
from app.models import (
    Recipe,
    Comment,
    CategoryEnum,
    Like,
    Favourite,
    User
)
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

        liked_recipe_ids = []

        if current_user.is_authenticated:
            liked_recipe_ids = [
                like.recipe_id for like in current_user.likes
            ]

        return render_template('index.html',
                             sections=sections,
                             total_recipes=total_recipes,
                             liked_recipe_ids=liked_recipe_ids,
                             error=None)

    except Exception as e:
        print("Database Error:", e)
        return render_template('index.html',
                             sections=[],
                             total_recipes=0,
                             liked_recipe_ids=[],
                             error=None)

@app.route("/recipes")
def recipes():
    return render_template("browse_recipes.html")


@app.route("/privacy_policy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms_and_condition")
def terms():
    return render_template("terms.html")


@app.route('/profile')
@login_required
def profile():
   
    # Gather all recipes owned by user, liked by user and favourited by users via relationships
    user_recipes = Recipe.query.filter_by(user_id=current_user.id).all()
    liked_recipes = [like.recipe for like in current_user.likes]
    fav_recipes = [fav.recipe for fav in current_user.favourites]

    user = {
        'name': current_user.username,
        'bio': current_user.bio or '',
        'profile_image': current_user.profile_image,
        'is_owner': True,
        'recipes_count': len(user_recipes),
        'likes_count': len(liked_recipes),
        'favourites_count': len(fav_recipes),
        'recipes': user_recipes,
        'likes': liked_recipes,
        'favourites': fav_recipes,
    }

    liked_recipe_ids = [like.recipe_id for like in current_user.likes]

    return render_template('profile.html', user=user, liked_recipe_ids=liked_recipe_ids)

@app.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
         
    #JSON payload from frontend edit profile modal
    data = request.get_json()
    new_name = data.get('name', '').strip()
    new_bio = data.get('bio', '').strip()
    new_avatar = data.get('profile_image', '').strip()

    # Ensure username is unique, but allow the user to keep their own username
    if new_name != current_user.username:
        existing = User.query.filter_by(username=new_name).first()
        if existing:
            return jsonify({'success': False, 'error': 'Username already taken'}), 409

    #update fields
    current_user.username = new_name
    current_user.bio = new_bio
    if new_avatar:
        current_user.profile_image = new_avatar

    db.session.commit()
    return jsonify({'success': True})


@app.route('/profile/delete', methods=['POST'])
@login_required
def delete_account():
    
    # Cascade in models.py handles deleting related recipes, likes, favourites, comments
    db.session.delete(current_user)
    db.session.commit()
    return jsonify({'success': True, 'redirect': url_for('home')})


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'GET':
        return render_template('signup.html')

    data = request.get_json()

    username = data.get('username', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    # Validation
    if not username or not email or not password:
        return jsonify({
            'success': False,
            'error': 'All fields are required'
        }), 400

    # Check existing username
    existing_username = User.query.filter_by(username=username).first()

    if existing_username:
        return jsonify({
            'success': False,
            'error': 'Username already taken'
        }), 409

    # Check existing email
    existing_email = User.query.filter_by(email=email).first()

    if existing_email:
        return jsonify({
            'success': False,
            'error': 'Email already registered'
        }), 409

    # Create user
    user = User(
        username=username,
        email=email
    )

    # Hash password
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    # Auto login after signup
    login_user(user)

    return jsonify({
        'success': True,
        'redirect': url_for('home')
    })

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    data = request.get_json()

    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        login_user(user)

        return jsonify({
            'success': True,
            'redirect': url_for('home')
        })

    return jsonify({
        'success': False,
        'error': 'Invalid email or password'
    }), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/post')
@login_required
def post():
    return render_template('post.html')

@app.route('/recipe/<int:id>', methods=['GET', 'POST'])
def recipe(id):

    recipe = Recipe.query.get_or_404(id)

    if request.method == 'POST':

        if not current_user.is_authenticated:
            return redirect(url_for('login'))

        comment_text = request.form.get('comment')

        if comment_text and comment_text.strip():

            new_comment = Comment(
                content=comment_text.strip(),
                user_id=current_user.id,
                recipe_id=recipe.id
            )

            db.session.add(new_comment)
            db.session.commit()

        return redirect(url_for('recipe', id=recipe.id))

    related_recipes = Recipe.query.filter(
        Recipe.id != recipe.id
    ).limit(4).all()

    return render_template(
        'recipe.html',
        recipe=recipe,
        related_recipes=related_recipes
    )

@app.route('/recipe/<int:id>/like', methods=['POST'])
@login_required
def like_recipe(id):
    # Handles like button interactions by adding/removing a like record
    # and synchronising frontend state with updated like count

     
    existing_like = Like.query.filter_by(user_id=current_user.id, recipe_id=id).first()
    
    if existing_like:
        # Like exists — user is unliking the recipe
        db.session.delete(existing_like)
        db.session.commit()
        return jsonify({'liked': False, 'likes': Like.query.filter_by(recipe_id=id).count()})
    else:
        # No like exists — user is liking the recipe
        new_like = Like(user_id=current_user.id, recipe_id=id)
        db.session.add(new_like)
        db.session.commit()

        # return updated state and new like count
        return jsonify({'liked': True, 'likes': Like.query.filter_by(recipe_id=id).count()})


@app.route('/edit_recipe/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    if recipe.user_id != current_user.id:
        return redirect(url_for('home'))

    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.ingredients = request.form['ingredients']
        recipe.instructions = request.form['instructions']
        recipe.category = request.form['category']
        recipe.image_file = request.form['image_url']

        db.session.commit()

        return redirect(url_for('recipe', id=recipe.id))

    return render_template('edit_recipe_page.html', recipe=recipe)

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