import uuid
import os

from flask import Flask
from flask import render_template, request, redirect, make_response, url_for
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from database import db_session, init_db
from login import login_manager
from models import User

app = Flask(__name__)

app.secret_key = "ssucuuh398nuwetubr33rcuhne"

login_manager.init_app(app)
init_db()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/myPlants', methods=['POST'])
@login_required
def my_plants():
    json_file = request.get_json()
    sensor = json_file['sensor']
    print(sensor)

    return 'OK'


@app.route('/login', methods=['GET', 'POST'])
def login():
    response = None
    if request.method == 'GET':
        response = make_response(render_template('login.html'))
    else:
        response = make_response(redirect(url_for('myaccount')))

        user = User.query.filter_by(username=request.form['login_username']).first()
        if user and check_password_hash(user.password, request.form['login_password']):
            user.login_id = str(uuid.uuid4())
            db_session.commit()
            login_user(user)
    return response


@app.route('/register', methods=['POST'])
def register():
    # if request.method == 'GET':
    #     return render_template('register.html')
    # else:
    username = request.form['register_username']
    password = generate_password_hash(request.form['register_password'])

    user = User(username=username, password=password)
    db_session.add(user)
    db_session.commit()
    return redirect(url_for('login'))


@app.route('/myAccount', methods=['GET', 'POST'])
@login_required
def myaccount():
    return render_template('myaccount.html')


@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    return render_template('checkout.html')

@app.route('/forumTopics', methods=['GET', 'POST'])
def forum_topics():
    return render_template('forum.html')


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
