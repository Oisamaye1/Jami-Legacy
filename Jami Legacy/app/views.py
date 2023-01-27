from app import app
from flask import render_template
import random

data = [
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

@app.route("/")
def index():
    products = data
    return render_template("index.html", products= products)

@app.route("/products")
def products():
    products = data
    return render_template("products.html", products= products)

@app.route("/carts")
def cart():
    return render_template("carts.html")


name = "Benjamin"
@app.route('/login')
def login():
    page = name
    return render_template('login.html', page= page)