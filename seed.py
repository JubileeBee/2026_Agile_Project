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
                ingredients='200g chocolate, 100g butter, 3 eggs, 150g sugar, 100g flour',
                instructions='Melt chocolate, mix ingredients, bake at 200C for 12 mins.',
                category=CategoryEnum.DESSERT,
                prep_time=10,
                notes='Best served warm with vanilla ice cream.',
                cook_time=30,
                difficulty=DifficultyEnum.MEDIUM,
                servings=4,
                image_file="chocolate_lava_cake.jpeg",
                user_id=1
            ),
            Recipe(
                title='Avocado Toast',
                description='Simple and delicious avocado toast with a poached egg.',
                ingredients='2 slices of bread, 1 ripe avocado, 2 eggs, salt, pepper, 1 tbsp lemon juice',
                instructions='Toast bread, mash avocado, poach egg, assemble.',
                category=CategoryEnum.BREAKFAST,
                prep_time=5,
                notes='Add chilli flakes for extra kick.',
                cook_time=10,
                difficulty=DifficultyEnum.EASY,
                servings=1,
                image_file="avocado_toast.jpeg",
                user_id=2
            ),
            Recipe(
                title='Soy Sauce Ramen',
                description='Rich and flavourful Japanese soy sauce ramen.',
                ingredients='100g ramen noodles, 2 tbsp soy sauce, 1 cup broth, 100g pork, 2 eggs, 2 green onions',
                instructions='Prepare broth, cook noodles, assemble toppings.',
                category=CategoryEnum.DINNER,
                prep_time=15,
                notes='Use homemade broth for best results.',
                cook_time=45,
                difficulty=DifficultyEnum.HARD,
                servings=2,
                image_file="soy_sauce_ramen.jpeg",
                user_id=3
            ),
            Recipe(
                title='Caesar Salad',
                description='Classic Caesar salad with homemade dressing.',
                ingredients='1 head of romaine lettuce, 50g parmesan, 100g croutons, 3 tbsp caesar dressing',
                instructions='Toss lettuce with dressing, add croutons and parmesan.',
                category=CategoryEnum.LUNCH,
                prep_time=10,
                notes='Make dressing fresh for best flavour.',
                cook_time=15,
                difficulty=DifficultyEnum.EASY,
                servings=2,
                image_file="caesar_salad.jpg",
                user_id=4
            ),
            Recipe(
                title='Mango Smoothie',
                description='Refreshing tropical mango smoothie.',
                ingredients='2 ripe mangos, 1 cup yogurt, 1 cup milk, 2 tbsp honey, 1 cup ice',
                instructions='Blend all ingredients until smooth.',
                category=CategoryEnum.DRINK,
                prep_time=5,
                notes='Use frozen mango for a thicker smoothie.',
                cook_time=5,
                difficulty=DifficultyEnum.EASY,
                servings=2,
                image_file="mango_smoothie.jpg",
                user_id=5
            ),
            Recipe(
                title='Banana Pancakes',
                description='Fluffy banana pancakes perfect for a lazy morning.',
                ingredients='2 ripe bananas, 1 cup flour, 3 eggs, 1 cup milk, 2 tbsp butter, 2 tbsp maple syrup',
                instructions='Mash bananas, mix batter, cook on griddle.',
                category=CategoryEnum.BREAKFAST,
                prep_time=10,
                notes='The riper the banana the sweeter the pancakes.',
                cook_time=20,
                difficulty=DifficultyEnum.EASY,
                servings=4,
                image_file="bananas_pancakes.jpg",
                user_id=1
            ),
            Recipe(
                title='Chicken Stir Fry',
                description='Quick and healthy chicken stir fry with vegetables.',
                ingredients='100g chicken, 1 bell pepper, 100g broccoli, 2 tbsp soy sauce, 2 cloves garlic, 1 tsp ginger',
                instructions='Stir fry chicken, add vegetables and sauce, serve with rice.',
                category=CategoryEnum.DINNER,
                prep_time=15,
                notes='Slice chicken thin for quicker cooking.',
                cook_time=25,
                difficulty=DifficultyEnum.EASY,
                servings=3,
                image_file="chicken_stirfry.jpeg",
                user_id=2
            ),
            Recipe(
                title='Eggs Benedict',
                description='Classic brunch dish with poached eggs and hollandaise sauce.',
                ingredients='2 English muffins, 100g ham, 2 eggs, 100ml hollandaise sauce',
                instructions='Toast muffins, poach eggs, make hollandaise, assemble.',
                category=CategoryEnum.BRUNCH,
                prep_time=15,
                notes='Fresh hollandaise makes all the difference.',
                cook_time=30,
                difficulty=DifficultyEnum.HARD,
                servings=2,
                image_file="eggs_benedict.jpeg",
                user_id=3
            ),
            Recipe(
                title='Granola Bar',
                description='Healthy homemade granola bars perfect for snacking.',
                ingredients='1 cup oats, 1/2 cup honey, 1/2 cup peanut butter, 1/2 cup chocolate chips, 1/2 cup nuts',
                instructions='Mix ingredients, press into pan, bake and cut into bars.',
                category=CategoryEnum.SNACK,
                prep_time=10,
                notes='Store in an airtight container for up to a week.',
                cook_time=20,
                difficulty=DifficultyEnum.EASY,
                servings=12,
                image_file="granola_bar.jpeg",
                user_id=4
            ),
            Recipe(
                title='Tiramisu',
                description='Classic Italian dessert with coffee and mascarpone.',
                ingredients='100g ladyfingers, 250g mascarpone, 4 eggs, 100g sugar, 1 cup coffee, 2 tbsp cocoa powder',
                instructions='Dip ladyfingers in coffee, layer with mascarpone cream, chill.',
                category=CategoryEnum.DESSERT,
                prep_time=20,
                notes='Refrigerate overnight for best results.',
                cook_time=40,
                difficulty=DifficultyEnum.MEDIUM,
                servings=6,
                image_file="tiramisu.jpeg",
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
            (1, 3), (1, 5), (2, 6),
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