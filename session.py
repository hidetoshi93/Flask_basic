#render_template: テンプレートの表示し方
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "testFlask"

#セッションのライフタイム設定
app.permanent_session_lifetime = timedelta(minutes= 1)

@app.route('/')
def hello_world():
    return render_template('home.html')

# POST, GET method
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            session["user"] = user_name
            session.permanent = True
            return redirect(url_for("hello_user"))

    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name}!</h1>"

    return render_template('login.html')
    
@app.route('/user/admin')
def hello_admin():
    return "<h1> Hello admin!</h1>"

@app.route('/user')
def  hello_user():
    if "user" in session:
        name = session["user"]
        return f"<h1> Hello {name}!</h1>"
    else:
        redirect(url_for("login"))
@app.route('/logout')
def  logout():
    if "user" in session:
        session.pop("user", None)
    return redirect(url_for("login"))
    
if __name__ == "__main__":
    app.run(debug=True)