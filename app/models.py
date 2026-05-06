import enum
from datetime import datetime, timezone

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


# ------------------ ENUMS ------------------

class CategoryEnum(enum.Enum):
    BREAKFAST = "Breakfast"
    BRUNCH = "Brunch"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACK = "Snack"
    DRINK = "Drink"


class DifficultyEnum(enum.Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


# ------------------ USER LOADER ------------------

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ------------------ USER ------------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(64),
        unique=True,
        nullable=False,
        index=True
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.String(256),
        nullable=False
    )

    bio = db.Column(db.Text)

    profile_image = db.Column(
        db.String(255),
        nullable=False,
        default='https://api.dicebear.com/7.x/avataaars/svg?seed=default'
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    recipes = db.relationship(
        'Recipe',
        back_populates='author',
        cascade='all, delete-orphan'
    )

    comments = db.relationship(
        'Comment',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    likes = db.relationship(
        'Like',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    favourites = db.relationship(
        'Favourite',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# ------------------ RECIPE ------------------

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

    category = db.Column(
        db.Enum(CategoryEnum),
        nullable=False
    )

    cook_time = db.Column(db.Integer)

    difficulty = db.Column(
        db.Enum(DifficultyEnum),
        nullable=False
    )

    servings = db.Column(db.Integer)

    image_file = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    author = db.relationship(
        'User',
        back_populates='recipes'
    )

    comments = db.relationship(
        'Comment',
        back_populates='recipe',
        cascade='all, delete-orphan'
    )

    likes = db.relationship(
        'Like',
        back_populates='recipe',
        cascade='all, delete-orphan'
    )

    favourites = db.relationship(
        'Favourite',
        back_populates='recipe',
        cascade='all, delete-orphan'
    )


# ------------------ COMMENT ------------------

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipe.id'),
        nullable=False
    )

    user = db.relationship(
        'User',
        back_populates='comments'
    )

    recipe = db.relationship(
        'Recipe',
        back_populates='comments'
    )


# ------------------ LIKE ------------------

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipe.id'),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    user = db.relationship(
        'User',
        back_populates='likes'
    )

    recipe = db.relationship(
        'Recipe',
        back_populates='likes'
    )

    __table_args__ = (
        db.UniqueConstraint(
            'user_id',
            'recipe_id',
            name='unique_user_recipe_like'
        ),
    )


# ------------------ FAVOURITE ------------------

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipe.id'),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    user = db.relationship(
        'User',
        back_populates='favourites'
    )

    recipe = db.relationship(
        'Recipe',
        back_populates='favourites'
    )

    __table_args__ = (
        db.UniqueConstraint(
            'user_id',
            'recipe_id',
            name='unique_user_recipe_favourite'
        ),
    )