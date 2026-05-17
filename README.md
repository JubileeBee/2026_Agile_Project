# CITS3403_Group_Project
Our 2026 group Agile Web Development Project

Contributors:
| UWA ID | Name | Github Username |
|--------|------|----------------|
| 23957309 | Abbey Boyle | JubileeBee |
| 24342062 | Vanessa Do | vanessado2005 |
| 22524461 | Nabeel Khan | Khanuwa |
| 24270483 | Ivy Qi | ivqly |


## Project Overview

CozyCravings is a web-based recipe sharing platform developed as part of our 2026 Agile Web Development Project.

The application allows users to browse, create, and interact with recipes through a clean and modern interface inspired by contemporary food and lifestyle platforms.

Core features currently include:

- User account system
- Recipe creation and management
- Recipe categorisation and difficulty filtering
- Dynamic ingredient management
- Likes and favourites system
- Responsive frontend design
- Profile pages and user interaction features

The project is built using:

- Flask (Python web framework)
- SQLAlchemy ORM
- SQLite database
- Jinja2 templating
- HTML, CSS, and JavaScript
- Bootstrap 5

The goal of the project is to develop a scalable full-stack web application while applying Agile development practices, collaborative workflows, version control, and modern frontend/backend design principles.

## How to run CozyCravings:
### 1. Clone the repository

```bash
git clone https://github.com/JubileeBee/2026_Agile_Project.git
cd 2026_Agile_Project
```

### 2. Set up virtual environment

Make sure you are in the project root directory, then copy and paste the following into your terminal:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

This activates the virtual environment. Once activated, install all dependencies:

```bash
pip install -r requirements.txt
```

> Note: If you install any new libraries, make sure you are inside the virtual environment and manually add the package and version to `requirements.txt`. Do NOT run `pip freeze > requirements.txt` as this may overwrite other versions.

To exit the virtual environment:

```bash
deactivate
```

### 3. Set up secret key

Generate a secret key by running:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Create a `.env` file in the project root and add:
```bash
SECRET_KEY=your-generated-key-here
```
> Note: `.env` is already listed in `.gitignore` so Git will not track it — your secret key stays on your machine only.


### 4. Set up the database

```bash
flask db init
flask db migrate
flask db upgrade
python seed.py
```

> Note: `flask db init` only needs to be run once when setting up for the first time. If you have already done this before, just run `flask db upgrade` and `python seeds.py`.

### 5. Run the app
```bash
python myapp.py
```
Then open your browser and navigate to `http://127.0.0.1:5000`

> Tip: You can also `Ctrl+Click` the link that appears in your terminal after running the app. To stop the app, press `Ctrl+C` in the terminal.

### 6. Run the tests

Make sure:
- the virtual environment is activated
- dependencies are installed
- you have two terminals open both in our venv (one will be used for our flask server, the other our tests, you can just open a separate terminal on your IDE and follow through with the following commands)

#### Prepare the database

Before running tests & setting up Flask server, ensure the database is up to date in each terminal (extra precaution), we run:

```bash
flask db upgrade
```

Not optional, Seed the database with test/sample data, this ensures data is definitly loaded within our venv (extra precaution):

```bash
python seed.py
```

Once these steps in our seed and db have been performed, we utilise one terminal to run our flask server.

We run:

```bash
flask run
```

#### Run unit tests, on the Terminal separate to our running Flask server

Unit tests can be run first, these tests are the quickest to run through:

```bash
pytest tests/units 
```

#### Run end-to-end Selenium tests

Selenium tests take longer than our Unit tests to run.

In that same terminal used to run our unit tests, we perform our Selenium test, run:

```bash
pytest tests/e2e 
```

After running all of our individual tests, we can run them in a culmulative state, ensuring these tests pass through together. Within your terminal you ran those two tests in, we than perform:

#### Run all tests

```bash
pytest 
```