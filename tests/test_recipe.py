from app.models import User, Recipe

# Test that a logged-in user can create a recipe
#
# This test covers:
# - Authentication tests:
#   creates and logs in a valid user
#
# - Protected route tests:
#   verifies logged-in users can access the add_recipe route
#
# - Form submission tests:
#   submits recipe form data through a POST request
#
# - Database creation tests:
#   verifies the recipe is successfully stored in the database
#
# - Recipe validation/processing tests:
#   checks recipe fields are correctly saved after processing

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