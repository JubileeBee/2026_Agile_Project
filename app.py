# Main Flask application handling server-side routing and rendering of Jinja2 templates.
# The @app.route decorators map specific URLs to the functions that render the HTML pages.

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/post')
def post():
    return render_template('post.html')

# Route for displaying a single recipe detail page
# The <int:id> allows dynamic URLs like /recipe/1, /recipe/2

@app.route('/recipe/<int:id>')
def recipe_detail(id):
    return render_template('recipe.html', recipe_id=id)

if __name__ == '__main__':
    app.run(debug=True)