import sqlite3

from flask import Flask, render_template, request, g, session, json
from constants import *
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'some_secret'


def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):

    db = getattr(g, '_database', None)
    if db:
        print("WERE CLOSED CONNECTION")
        db.close()


def query_db(query, args=(), commit=False, one=False):
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    if commit:
        db.commit()
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/', methods=["GET", "POST"])
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def login():
    log = request.form["login"]
    password = request.form["password"]


@app.route('/register', methods=["GET", "POST"])
def register():

    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        with app.app_context():
            email = form.login.data
            password = form.password.data
            if query_db('select * from tUsers where username= ?', [email], one=True):
                #return json.jsonify(message="")
                return render_template('regResult.html', message="This E-Mail already used. Maybe, it's you?!")
            else:
                query_db('insert into tUsers (username, password) VALUES (?, ?)',
                        (email, password), True)
                session['logged_in'] = True
                session['username'] = email
                return render_template('regResult.html', message='SUCCESS!')
                #return json.jsonify(message="Success!")


if __name__ == '__main__':
    app.run()
