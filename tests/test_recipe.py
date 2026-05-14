from app.models import User, Recipe

# Test that a logged-in user can create a recipe
# Creates a test user and logs them in
# Submits recipe form data to the add_recipe route
# Verifies that the recipe is stored in the database

def test_create_recipe(client):

    # Create test user
    client.post(
        "/signup",
        json={
            "username": "chefuser",
            "email": "chef@example.com",
            "password": "password123"
        }
    )

    # Login test user
    client.post(
        "/login",
        json={
            "email": "chef@example.com",
            "password": "password123"
        }
    )

    # Submit recipe form
    response = client.post(
        "/add_recipe",
        data={
            "title": "Test Pasta",
            "description": "Delicious pasta recipe",
            "ingredient_name[]": ["Pasta"],
            "ingredient_quantity[]": ["200"],
            "ingredient_unit[]": ["g"],
            "instructions": "Cook pasta and serve",
            "category": "DINNER",
            "difficulty": "EASY",
            "prep_time": "10",
            "cook_time": "15",
            "servings": "2",
            "notes": "Test notes"
        },
        follow_redirects=True
    )

    assert response.status_code == 200

    recipe = Recipe.query.filter_by(title="Test Pasta").first()

    assert recipe is not None
    assert recipe.description == "Delicious pasta recipe"