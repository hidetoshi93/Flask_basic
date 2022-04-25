#render_template: テンプレートの表示し方

from unicodedata import name
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

# POST, GET method
@app.route('/login', method=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        if user_name:
            return redirect(url_for("hello_user"), name = user_name)
    return render_template('login.html')

@app.route('/user/admin')
def hello_admin():
    return "<h1> Hello admin!</h1>"

@app.route('/user/<name>')
def  hello_user(name):
    if name == 'admin':
        # redirect(hello_admin())
        redirect(url_for('hello_admin'))

    return f"<h1> Hello {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)