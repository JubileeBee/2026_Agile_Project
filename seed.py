import random
from app import app, db
from app.models import User, Recipe, Like, Favourite, Comment, CategoryEnum, DifficultyEnum

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # ------------------ USERS ------------------
        users = [
            User(username='emma_doe', email='emma@example.com', bio='I love baking and trying new recipes!',
                 profile_image='https://api.dicebear.com/7.x/thumbs/svg?seed=Destiny&backgroundColor=DDB892&shapeColor=7F5539'),
            User(username='jake_lee', email='jake@example.com', bio='Home cook and food enthusiast.',
                 profile_image='https://api.dicebear.com/7.x/thumbs/svg?seed=Aidan&backgroundColor=DDB892&shapeColor=7F5539'),
            User(username='mia_chen', email='mia@example.com', bio='Asian fusion is my specialty!',
                 profile_image='https://api.dicebear.com/7.x/thumbs/svg?seed=Kimberly&backgroundColor=DDB892&shapeColor=7F5539'),
            User(username='tom_hill', email='tom@example.com', bio='BBQ master and grill enthusiast.',
                 profile_image='https://api.dicebear.com/7.x/thumbs/svg?seed=Lilliana&backgroundColor=DDB892&shapeColor=7F5539'),
            User(username='sara_kim', email='sara@example.com', bio='Healthy eating advocate.',
                 profile_image='https://api.dicebear.com/7.x/thumbs/svg?seed=Avery&backgroundColor=DDB892&shapeColor=7F5539'),
        ]

        for user in users:
            user.set_password('password123')

        db.session.add_all(users)
        db.session.commit()

        # ------------------ RECIPES ------------------
        recipes = [
            Recipe(
                title='Chocolate Lava Cake',
                description='A decadent chocolate cake with a gooey molten center.',
                ingredients='Chocolate, butter, eggs, sugar, flour',
                instructions='Melt chocolate, mix ingredients, bake at 200C for 12 mins.',
                category=CategoryEnum.DESSERT,
                cook_time=30,
                difficulty=DifficultyEnum.MEDIUM,
                servings=4,
                image_file='https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=400',
                user_id=1
            ),
            Recipe(
                title='Avocado Toast',
                description='Simple and delicious avocado toast with a poached egg.',
                ingredients='Bread, avocado, eggs, salt, pepper, lemon',
                instructions='Toast bread, mash avocado, poach egg, assemble.',
                category=CategoryEnum.BREAKFAST,
                cook_time=10,
                difficulty=DifficultyEnum.EASY,
                servings=1,
                image_file='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPfqIDCCdL5IDo0IOwcXdOx6q8o7V6su_lCg&s',
                user_id=2
            ),
            Recipe(
                title='Soy Sauce Ramen',
                description='Rich and flavourful Japanese soy sauce ramen.',
                ingredients='Ramen noodles, soy sauce, broth, pork, eggs, green onions',
                instructions='Prepare broth, cook noodles, assemble toppings.',
                category=CategoryEnum.DINNER,
                cook_time=45,
                difficulty=DifficultyEnum.HARD,
                servings=2,
                image_file='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLQxLm2PI5YnBZFuK-V8K6hDKFkrMTI0uDoA&s',
                user_id=3
            ),
            Recipe(
                title='Caesar Salad',
                description='Classic Caesar salad with homemade dressing.',
                ingredients='Romaine lettuce, parmesan, croutons, caesar dressing',
                instructions='Toss lettuce with dressing, add croutons and parmesan.',
                category=CategoryEnum.LUNCH,
                cook_time=15,
                difficulty=DifficultyEnum.EASY,
                servings=2,
                image_file='https://bakerbynature.com/wp-content/uploads/2025/01/Caesar-Salad-9.jpg',
                user_id=4
            ),
            Recipe(
                title='Mango Smoothie',
                description='Refreshing tropical mango smoothie.',
                ingredients='Mango, yogurt, milk, honey, ice',
                instructions='Blend all ingredients until smooth.',
                category=CategoryEnum.DRINK,
                cook_time=5,
                difficulty=DifficultyEnum.EASY,
                servings=2,
                image_file='https://twosleevers.com/wp-content/uploads/2025/05/Mango-Smoothie-1.jpg',
                user_id=5
            ),
            Recipe(
                title='Banana Pancakes',
                description='Fluffy banana pancakes perfect for a lazy morning.',
                ingredients='Bananas, flour, eggs, milk, butter, maple syrup',
                instructions='Mash bananas, mix batter, cook on griddle.',
                category=CategoryEnum.BREAKFAST,
                cook_time=20,
                difficulty=DifficultyEnum.EASY,
                servings=4,
                image_file='https://lmld.org/wp-content/uploads/2010/02/banana-pancakes-3.jpg',
                user_id=1
            ),
            Recipe(
                title='Chicken Stir Fry',
                description='Quick and healthy chicken stir fry with vegetables.',
                ingredients='Chicken, bell peppers, broccoli, soy sauce, garlic, ginger',
                instructions='Stir fry chicken, add vegetables and sauce, serve with rice.',
                category=CategoryEnum.DINNER,
                cook_time=25,
                difficulty=DifficultyEnum.EASY,
                servings=3,
                image_file='https://images.unsplash.com/photo-1512058564366-18510be2db19?w=400',
                user_id=2
            ),
            Recipe(
                title='Eggs Benedict',
                description='Classic brunch dish with poached eggs and hollandaise sauce.',
                ingredients='English muffins, ham, eggs, hollandaise sauce',
                instructions='Toast muffins, poach eggs, make hollandaise, assemble.',
                category=CategoryEnum.BRUNCH,
                cook_time=30,
                difficulty=DifficultyEnum.HARD,
                servings=2,
                image_file='https://images.unsplash.com/photo-1608039829572-78524f79c4c7?w=400',
                user_id=3
            ),
            Recipe(
                title='Granola Bar',
                description='Healthy homemade granola bars perfect for snacking.',
                ingredients='Oats, honey, peanut butter, chocolate chips, nuts',
                instructions='Mix ingredients, press into pan, bake and cut into bars.',
                category=CategoryEnum.SNACK,
                cook_time=20,
                difficulty=DifficultyEnum.EASY,
                servings=12,
                image_file='https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=400',
                user_id=4
            ),
            Recipe(
                title='Tiramisu',
                description='Classic Italian dessert with coffee and mascarpone.',
                ingredients='Ladyfingers, mascarpone, eggs, sugar, coffee, cocoa powder',
                instructions='Dip ladyfingers in coffee, layer with mascarpone cream, chill.',
                category=CategoryEnum.DESSERT,
                cook_time=40,
                difficulty=DifficultyEnum.MEDIUM,
                servings=6,
                image_file='https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400',
                user_id=5
            ),
        ]

        db.session.add_all(recipes)
        db.session.commit()

        # ------------------ LIKES ------------------
        like_pairs = [
            (1, 2), (1, 3), (1, 4), (2, 1), (2, 5),
            (3, 1), (3, 6), (4, 2), (4, 7), (5, 3),
            (5, 8), (1, 9), (2, 10), (3, 4), (4, 6)
        ]

        for user_id, recipe_id in like_pairs:
            db.session.add(Like(user_id=user_id, recipe_id=recipe_id))

        db.session.commit()

        # ------------------ FAVOURITES ------------------
        fav_pairs = [
            (1, 3), (1, 5), (2, 2), (2, 6),
            (3, 7), (4, 1), (5, 4), (5, 9)
        ]

        for user_id, recipe_id in fav_pairs:
            db.session.add(Favourite(user_id=user_id, recipe_id=recipe_id))

        db.session.commit()

        # ------------------ COMMENTS ------------------
        comments = [
            Comment(content='This is absolutely delicious!', user_id=2, recipe_id=1),
            Comment(content='Made this for breakfast, loved it!', user_id=3, recipe_id=2),
            Comment(content='Best ramen I have ever made at home!', user_id=1, recipe_id=3),
            Comment(content='Simple and tasty, will make again.', user_id=5, recipe_id=4),
            Comment(content='So refreshing on a hot day!', user_id=4, recipe_id=5),
        ]

        db.session.add_all(comments)
        db.session.commit()

        print("Seed data added successfully!")

if __name__ == '__main__':
    seed_data()