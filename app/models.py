```python
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


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
        nullable=False
    )

    password_hash = db.Column(
        db.String(256),
        nullable=False
    )

    bio = db.Column(
        db.Text,
        nullable=True
    )

    profile_image = db.Column(
        db.String(50),
        nullable=False,
        default='avatar1.png'
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

    favorites = db.relationship(
        'Favorite',
        back_populates='user',
        cascade='all, delete-orphan'
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    ingredients = db.Column(
        db.Text,
        nullable=False
    )

    instructions = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        nullable=True
    )

    image_file = db.Column(
        db.String(255),
        nullable=True
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

    favorites = db.relationship(
        'Favorite',
        back_populates='recipe',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Recipe {self.title}>'


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

    def __repr__(self):
        return f'<Comment {self.id}>'


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

    def __repr__(self):
        return f'<Like {self.id}>'


class Favorite(db.Model):
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

    user = db.relationship(
        'User',
        back_populates='favorites'
    )

    recipe = db.relationship(
        'Recipe',
        back_populates='favorites'
    )

    __table_args__ = (
        db.UniqueConstraint(
            'user_id',
            'recipe_id',
            name='unique_user_recipe_favorite'
        ),
    )

    def __repr__(self):
        return f'<Favorite {self.id}>'
```
