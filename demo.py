from flask import Flask, redirect, url_for

# redirect + url_for: URLにアクセスしたユーザーを別のURLに誘導する

app = Flask(__name__)
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