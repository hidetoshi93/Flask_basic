#render_template: テンプレートの表示し方
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config["SECRET_KEY"] = "testFlask"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#セッションのライフタイム設定
app.permanent_session_lifetime = timedelta(minutes= 1)

db = SQLAlchemy(app)

@app.route('/home')

@app.route('/')
def home():
    return render_template('home.html')

# POST, GET method
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            session["user"] = user_name
            session.permanent = True
            flash("You logged in succesfully!", "info")
            return render_template("user.html", user = user_name)

    if "user" in session:
        name = session["user"]
        flash("You have already logged in!", "info")
        return render_template("user.html", user = name)

    return render_template('login.html')
    
@app.route('/user/admin')
def hello_admin():
    return "<h1> Hello admin!</h1>"

@app.route('/user')
def  hello_user():
    if "user" in session:
        name = session["user"]
        return render_template("user.html", user = name)
    else:
        flash ("You haven't logged in!", "info")
        return redirect(url_for("login"))
@app.route('/logout')
def  logout():
    if "user" in session:
        flash("You logged out!", "info")
        session.pop("user", None)
        return redirect(url_for("login"))
    
if __name__ == "__main__":
    if not path.exists("user.db"):
        db.create_all(app = app)
        print("Created database")

    app.run(debug=True)