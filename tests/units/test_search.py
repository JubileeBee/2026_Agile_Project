# AJAX live-search tests will be added after
# feature/ajax-live-search PR#70 is merged into main

from app.models import Recipe


# Test AJAX live search endpoint
#
# This test covers:
# - AJAX/API endpoint tests:
#   sends a GET request to the live-search JSON route
#
# - Search/filter functionality tests:
#   verifies recipes can be searched by title
#
# - JSON response tests:
#   checks that recipe data is returned correctly as JSON
#
# - Database retrieval tests:
#   confirms stored recipes are retrieved from the database

def test_live_search(client):

    # Create and login test user
    client.post(
        "/signup",
        json={
            "username": "searchuser",
            "email": "search@example.com",
            "password": "password123"
        }
    )

    client.post(
        "/login",
        json={
            "email": "search@example.com",
            "password": "password123"
        }
    )

    # Create recipe
    client.post(
        "/add_recipe",
        data={
            "title": "Chocolate Cake",
            "description": "Rich chocolate dessert",
            "ingredient_name[]": ["Chocolate"],
            "ingredient_quantity[]": ["200"],
            "ingredient_unit[]": ["g"],
            "instructions": "Bake cake",
            "category": "DESSERT",
            "difficulty": "EASY",
            "prep_time": "15",
            "cook_time": "30",
            "servings": "4",
            "notes": "Test dessert"
        },
        follow_redirects=True
    )

    # Call AJAX search endpoint
    response = client.get("/api/live-search?q=Chocolate")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) > 0
    assert data[0]["title"] == "Chocolate Cake"