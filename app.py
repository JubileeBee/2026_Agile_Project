from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google    

app = Flask(__name__)

app.secret_key = "your-secret-key"
google_bp = make_google_blueprint(
    client_id="your-google-client-id", 
    client_secret="your-google-client-secret", 
    redirect_to="google_login")

app.register_blueprint(
    google_bp, 
    url_prefix="/signup")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route("/login/google")
def google_login():
    return redirect("/google-oauth-start")

@app.route("/login/facebook")
def facebook_login():
    return redirect("/facebook-oauth-start")

@app.route("/google-authorized") 
def google_authorized():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    user_data = resp.json()

    email = user_data["email"]
    user = User.query.filter_by(email=email).first()
    if user: 
        #existing user, log them in
        login_user(user)
    else:
        #new user, create an account and log them in
        new_user = User(email=email)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
    return redirect(url_for("dashboard"))

app.run(debug=True)