def test_signup_page_loads(client):
    response = client.get("/signup")

    assert response.status_code == 200

    from app.models import User


# Purpose: Test that a new user can successfully sign up
# RequestType: Sends a POST request to the /signup route with test user data
# Validation Goals: 
# Verifies:
# 1. The request returns a successful response
# 2. The user is actually created in the test database
# 3. The stored username matches the submitted username

from app.models import User


def test_user_signup(client):
    response = client.post(
        "/signup",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    user = User.query.filter_by(email="test@example.com").first()

    assert user is not None
    assert user.username == "testuser"

    
# Test that duplicate email registration is rejected
# Creates a first user successfully
# Attempts to register another user with the same email
# Verifies that the server returns an error response

def test_duplicate_email_signup(client):

    # First signup
    client.post(
        "/signup",
        json={
            "username": "user1",
            "email": "duplicate@example.com",
            "password": "password123"
        }
    )

    # Duplicate signup attempt
    response = client.post(
        "/signup",
        json={
            "username": "user2",
            "email": "duplicate@example.com",
            "password": "password456"
        }
    )

    assert response.status_code == 409

# Test successful login with valid credentials
# Creates a user in the test database
# Sends a login request with correct email and password
# Verifies that login succeeds

def test_successful_login(client):

    # Create test user
    client.post(
        "/signup",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "password123"
        }
    )

    # Attempt login
    response = client.post(
        "/login",
        json={
            "email": "login@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


# Test failed login with incorrect password
# Verifies that invalid credentials are rejected

def test_failed_login(client):

    # Create test user
    client.post(
        "/signup",
        json={
            "username": "wrongpassuser",
            "email": "wrong@example.com",
            "password": "correctpassword"
        }
    )

    # Attempt login with wrong password
    response = client.post(
        "/login",
        json={
            "email": "wrong@example.com",
            "password": "incorrectpassword"
        }
    )

    assert response.status_code == 401

    data = response.get_json()

    assert data["success"] is False