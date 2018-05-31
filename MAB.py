import sqlite3

from flask import Flask, render_template, request, g
from flask import session

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect()


@app.route('/', methods=["GET", "POST"])
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def login():
    print("HERE")
    print(request)
    log = request.form["login"]
    password = request.form["password"]
    print(log, password)


@app.route('/register', methods=["POST"])
def register():
    print("HERE")
    print(request)
    log = request.form["login"]
    password = request.form["password"]
    print(log, password)

if __name__ == '__main__':
    app.run()
