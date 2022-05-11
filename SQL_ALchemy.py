#render_template: テンプレートの表示し方
# fix error ImportError: DLL load failed while importing _sqlite3
# 参考　https://qiita.com/saito-h/items/9c9f73e39ac205c0aebf


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

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)

    # nameの最長は100
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/home')

@app.route('/')
def home():
    return render_template('home.html')

# POST, GET method
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            flash("You logged in succesfully!", "info")
            return redirect(url_for("user"))

    if "user" in session:
        name = session["user"]
        flash("You have already logged in!", "info")
        return redirect(url_for("user"))

    return render_template('login.html')
    
@app.route('/user/admin')
def hello_admin():
    return "<h1> Hello admin!</h1>"

@app.route('/user')
def  user():
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