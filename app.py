from flask import Flask

app = Flask(__name__)

@app.route('/user')
def  hello_world():
     return "test"

if __name__ == "__main__":
    app.run()