from flask import Flask, redirect, url_for

# redirect: URLにアクセスしたユーザーを別のURLに誘導する
# url_for


app = Flask(__name__)

@app.route('/user')
def  hello_world():
     return "test"

if __name__ == "__main__":
    app.run()