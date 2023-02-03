from flask import Flask, render_template, request
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
moment = Moment(app)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


from app import views
from app import login