from flask import Flask

app = Flask(__name__)


@app.route("/add/user")
def add_user():
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port='8000')
