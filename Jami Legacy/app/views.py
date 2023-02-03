from app import app, db
from flask import render_template, request, redirect, flash, url_for
import random
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email


productInfo = [
  {
    "name": "MEN'S NIKE AIR FORCE 1",
    "price": "100",
    "sex": "Male",
    "image": "https://media.finishline.com/i/finishline/CW2288_111_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Nike"
    },
  {
    "name": "NIKE AIR MAX 270",
    "price": "170",
    "sex": "Female",
    "image": "https://media.finishline.com/i/finishline/6298394_002_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Nike",
    },
  {
    "name": "AIR JORDAN RETRO 1",
    "price": "140",
    "sex": "Male",
    "image": "https://media.finishline.com/i/finishline/DQ8426_060_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Jordan"
    },
  {
    "name": "ADIDAS ORIGINALS OZWEEGO",
    "price": "100",
    "sex": "Male",
    "image": "https://media.finishline.com/i/finishline/HP9117_034_P1?$default$&$global_badge_pdp$&layer0=[h=671&w=671&bg=rgb(237,237,237)]&h=671&w=671",
    "brand": "Adidas",
    },
  {
    "name": "AIR JORDAN RETRO 1",
    "price": "125",
    "sex": "Female",
    "image": "https://media.finishline.com/i/finishline/BQ6472_061_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Jordan",
   },
  {
    "name": "AIR JORDAN RETRO 13",
    "price": "200",
    "sex": "Male",
    "image": "https://media.finishline.com/i/finishline/DJ5982_041_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Jordan",
    },
  {
    "name": "MEN'S NEW BALANCE 2002R",
    "price": "140",
    "sex": "Male",
    "image": "https://media.finishline.com/i/finishline/M2002RJM_081_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "New Balance",
    },
  {
    "name": "CONVERSE RUN STAR MOTION",
    "price": "120",
    "sex": "Female",
    "image": "https://media.finishline.com/i/finishline/171545C_001_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Converse",
    },
  {
    "name": "CONVERSE RUN STAR HIKE",
    "price": "110",
    "sex": "Female",
    "image": "https://media.finishline.com/i/finishline/166799C_102_P1?$default$&w=671&&h=671&bg=rgb(237,237,237)",
    "brand": "Converse",
    },
  {
    "name": "TIMBERLAND 6 INCH",
    "price": "210",
    "sex": "Male",
    "image": "https://media.finishline.com/i/finishline/10073_BLK_P1?$default$&$transparent_badge$&layer0=[h=671&w=671&bg=rgb(237,237,237)]&h=671&w=671",
    "brand": "Timberland",
    }
]

class Users(db.Model):
  __tablename__ = "users"
  id = db.Column('student_id', db.Integer, primary_key = True)
  firstname = db.Column("first_name",  db.String(40))
  lastname = db.Column("last_name",  db.String(40))
  username = db.Column("username",  db.String(40), unique=True)
  password = db.Column("password", db.String(30))
  email = db.Column("email", db.String(30))

def __init__(self, firstname, lastname, username, password, email):
   self.firstname = firstname
   self.lastname = lastname
   self.username = username
   self.password = password
   self.email = email

def __str__(self):
        return '<User %r>' % [self.firstname, self.lastname, self.username, self.password, self.email]

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField('Submit')

class Signup(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=30)])
    username = StringField('Username', validators=[DataRequired(), Length(min=8, max=30)])
    email = EmailField('Email Address', validators=[DataRequired(), Email(), Length(max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField('Submit')

currentUser = None

@app.route("/")
def index():
    products = productInfo
    currentUser = username
    return render_template("index.html", products= products,
    current_time = datetime.utcnow())

@app.route("/products")
def products():
    products = productInfo
    
    return render_template("products.html", products= products)

@app.route("/carts")
def cart():
    return render_template("carts.html")


@app.route('/login', methods=["GET", "POST"])
def login():
  username = ""
  form = Login()
  if request.method == 'POST' and form.validate():

    if Users.query.filter_by(username=form.username.data).all() and Users.query.filter_by(password=form.password.data).all():
      username = form.username.data
      return username, redirect("/")

    else:
      flash("Incorrect username or password")
      
  return render_template('login.html', username=username, form = form)

@app.route('/signup', methods=["GET", "POST"])
def signup():
  username = ""
  form = Signup()

  if request.method == 'POST' and form.validate():
    if Users.query.filter_by(username=form.username.data).all():
      flash("Username already exist")
    
    else:
      username = form.username.data
      new_users = Users(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, password=form.password.data, email=form.email.data)
      db.session.add(new_users)
      db.session.commit()
  return render_template('signup.html', username=username, form = form)

@app.route('/profile/<username>')
def profile(username):
  user = get_user_from_database(username)

  return render_template('profile.html', user = user )


def get_user_from_database(user_name):
    user = [user for user in Users.query.filter_by(username=user_name).all() 
    if user.username == user_name]
    return user[0] if user else None

