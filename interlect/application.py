# python -m flask run

from flask import render_template, Flask, Response, redirect, url_for, request, abort
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_login import current_user
from Models.User import User
from Models.AppBase import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database
engine = create_engine('sqlite:///Database/database.sqlite3')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Flask app
app = Flask(__name__)

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
@app.route('/home')
def home():
    if current_user.get_id() != None:
        return redirect(url_for('userPage', id=current_user.get_id()))
    return render_template('home.html')

@app.route("/login", methods=["POST"])
def login_post():
    curUser = (request.form['username'], request.form['password'])
    users = session.query(User).with_entities(User.username, User.password).all()
    if curUser in users:
        user = session.query(User).filter(User.username == curUser[0], User.password == curUser[1]).first()
        login_user(user)
        return redirect(url_for('userPage', id=user.id))
    else:
        return abort(401)

@app.route("/login", methods=["GET"])
def login_get():
    if current_user.get_id() != None:
        return redirect(url_for('userPage', id=current_user.get_id()))
    return render_template('login.html')

@app.route("/signup", methods=["POST"])
def signup_post():
    if current_user.get_id() != None:
        return redirect(url_for('userPage', id=current_user.get_id()))
    signup_input = (request.form['username'], request.form['password'], request.form['confirm_password'])
    user = session.query(User).filter(User.username ==signup_input[0]).first()
    if signup_input[1] != signup_input[2]:
        return redirect(url_for('signup'))
    elif len(signup_input[0]) == 0 or len(signup_input[1]) < 4:
        return redirect(url_for('signup'))
    elif user != None:
        return redirect(url_for('signup_get'))
    else:
        newUser = User(username=signup_input[0], password=signup_input[1])
        session.add(newUser)
        session.commit()
        login_user(newUser)
        return redirect(url_for('userPage', id=current_user.get_id()))

@app.route("/signup",methods=["GET"])
def signup_get():
    if current_user.get_id() != None:
        return redirect(url_for('userPage', id=current_user.get_id()))
    return render_template('signin.html')

@app.route('/user/<int:id>')
@login_required
def userPage(id):
    if int(current_user.get_id()) != id:
        return redirect(url_for('home'))
    user = session.query(User).filter(User.id == id).first()
    return render_template('user_page.html',username=user.username)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    user = session.query(User).filter(User.id == int(userid)).first()
    return user

if __name__ == "__main__":
    app.run()
