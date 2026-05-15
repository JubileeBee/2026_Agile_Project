from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test 1
# Selenium test for homepage loading
#
# This test covers:
# - Browser automation testing
# - Frontend page loading
# - Basic UI rendering validation

def test_homepage_loads():

    driver = webdriver.Chrome()

    driver.get("http://127.0.0.1:5000/")

    time.sleep(2)

    assert "Recipe" in driver.page_source or "recipe" in driver.page_source

    driver.quit()

# Test 2
# Selenium test for user login
#
# This test covers:
# - Browser automation testing
# - Login form interaction
# - Frontend user authentication flow
# - Form submission testing
# - Page navigation after login

def test_login_flow():

    driver = webdriver.Chrome()

    # Open login page
    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    # Enter login credentials
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("emma@example.com")
    password_input.send_keys("password123")

    # Submit form
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    time.sleep(3)

    # Verify redirect after login
    assert "login" not in driver.current_url.lower()

    driver.quit()

# Test 3
# Selenium test for recipe creation
#
# This test covers:
# - Browser automation testing
# - Authenticated user actions
# - Recipe form interaction
# - Frontend/backend integration
# - Recipe submission workflow
# - Database-backed content creation

def test_create_recipe():

    driver = webdriver.Chrome()

    # Open login page
    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    # Enter login credentials
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("emma@example.com")
    password_input.send_keys("password123")

    # Submit login form
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    submit_button.click()

    time.sleep(2)

    # Open add recipe page
    driver.get("http://127.0.0.1:5000/add_recipe")

    time.sleep(2)

    # Fill recipe form
    driver.find_element(By.ID, "title").send_keys(
        "Selenium Test Recipe"
    )

    driver.find_element(By.ID, "description").send_keys(
        "Recipe created during Selenium testing"
    )

    driver.find_element(By.ID, "prep_time").send_keys("10")

    driver.find_element(By.ID, "cook_time").send_keys("20")

    driver.find_element(By.ID, "servings").send_keys("4")

    # Select category
    category_select = driver.find_element(By.ID, "category")
    category_select.send_keys("Dinner")

    # Select difficulty
    difficulty_select = driver.find_element(By.ID, "difficulty")
    difficulty_select.send_keys("Easy")

    # Fill ingredient fields
    driver.find_element(
        By.NAME,
        "ingredient_name[]"
    ).send_keys("Flour")

    driver.find_element(
        By.NAME,
        "ingredient_quantity[]"
    ).send_keys("2")

    driver.find_element(
        By.NAME,
        "ingredient_unit[]"
    ).send_keys("cups")

    # Fill instructions
    driver.find_element(By.ID, "instructions").send_keys(
        "Mix ingredients and cook."
    )
# Scroll to submit button
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        submit_button
    )

    time.sleep(1)

    # Submit recipe
    driver.execute_script(
        "arguments[0].click();",
        submit_button
    )
    time.sleep(3)

    # Verify recipe appears
    assert "Selenium Test Recipe" in driver.page_source

    driver.quit()


# Test 4
# Selenium test for recipe search
#
# This test covers:
# - Browser automation testing
# - Search form interaction
# - Frontend search functionality
# - Dynamic content filtering
# - User navigation workflow

def test_recipe_search():

    driver = webdriver.Chrome()

    # Open homepage
    driver.get("http://127.0.0.1:5000/")

    time.sleep(2)

    # Locate search input
    search_input = driver.find_element(By.NAME, "q")

    # Enter search query
    search_input.send_keys("Pasta")

    # Submit search
    search_input.submit()

    time.sleep(3)

    # Verify search results page loads
    assert "Pasta" in driver.page_source

    driver.quit()

# Test 5
# Selenium test for protected route access
#
# This test covers:
# - Browser automation testing
# - Route protection validation
# - User authentication enforcement
# - Frontend security behaviour
# - Redirect handling for unauthenticated users

def test_protected_route_requires_login():

    driver = webdriver.Chrome()

    # Attempt to access protected page
    driver.get("http://127.0.0.1:5000/add_recipe")

    time.sleep(2)

    # Verify redirect to login page
    assert "login" in driver.current_url.lower()

    driver.quit()

# Test 6
# Selenium test for user logout
#
# This test covers:
# - Browser automation testing
# - User session management
# - Logout functionality
# - Authentication state changes
# - Frontend navigation after logout

def test_logout_flow():

    driver = webdriver.Chrome()

    # Open login page
    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    # Enter login credentials
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("emma@example.com")
    password_input.send_keys("password123")

    # Submit login form
    submit_button = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    submit_button.click()

    time.sleep(2)

    # Open logout route
    driver.get("http://127.0.0.1:5000/logout")

    time.sleep(2)

    # Verify redirect after logout
    assert driver.current_url == "http://127.0.0.1:5000/"

    driver.quit()