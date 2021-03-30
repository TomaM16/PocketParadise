from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, LoginManager, current_user, login_required, logout_user
from flask_security import UserMixin
import datetime

app = Flask(__name__)
app.secret_key = "teenovator_PocketParadise"
#login_manager = LoginManager(app)

file_path = os.path.abspath(os.getcwd())+"/PocketParadise.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + file_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def is_active(self):
        return True
'''
db.create_all()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/myPlants', methods=['POST'])
def my_plants():
    json_file = request.get_json()
    sensor = json_file['sensor']
    print(sensor)

    return 'OK'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('login_username')
        password = request.form.get('login_password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('user', username=current_user.username))
        else:
            flash('Invalid password!', 'error')
            return redirect(url_for('login'))
    else:
        return render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        user1 = User.query.filter_by(username=name).first()

        if user:
            flash('This email exists!', 'error')
            return redirect(url_for('register'))
        elif user1:
            flash('This username exists!', 'error')
            return redirect(url_for('register'))
        elif password != confirm_password:
            flash('Your passwords are not the same!', 'error')
            return redirect(url_for('register'))
        elif len(email) == 0 or len(name) == 0 or len(password) == 0 or len(confirm_password) == 0:
            flash('You are trying to add an empty margin!', 'error')
            return redirect(url_for('register'))

        else:
            new_user = User(name, email, password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))

    else:
        return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
