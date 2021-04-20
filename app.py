import uuid
import os

from flask import Flask, jsonify
from flask import render_template, request, redirect, make_response, url_for
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from database import db_session, init_db
from login import login_manager
from models import User, Tag, Question, Comment

app = Flask(__name__)

app.secret_key = "ssucuuh398nuwetubr33rcuhne"

login_manager.init_app(app)
init_db()


sensor = None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/myPlants', methods=['GET', 'POST'])
# @login_required
def my_plants():
    global sensor
    if request.method == 'POST':
        print(1)
        json_file = request.get_json()
        print(2)
        sensor = json_file['sensor']
        print(3)
        print(sensor)

    return render_template('myplants.html', sensor=sensor)


@app.route('/forum', methods=['GET', 'POST'])
def forum():
    return render_template('forum.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    response = None
    if request.method == 'GET':
        response = make_response(render_template('login.html'))
    else:
        response = make_response(redirect(request.referrer[:-5]))  # TODO fix to go back to previous page

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


@app.route('/addPost', methods=['GET', 'POST'])
@login_required
def add_post():
    return render_template('add.html')


@app.route('/myAccount', methods=['GET', 'POST'])
@login_required
def my_account():
    return render_template('myaccount.html')


@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    return render_template('checkout.html')


@app.route('/forumTopics', methods=['GET', 'POST'])
def forum_topics():
    return render_template('forum.html')


# @app.route('/<topic_name/like>', method=['POST'])
# @login_required
# def like(topic_id, user_id):
#     if request.method == 'POST':
#         topic = Topic.query.filter_by(topic_id=topic_id)


if __name__ == '__main__':
    app.run()
