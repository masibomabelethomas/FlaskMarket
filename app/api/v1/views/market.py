from app.api.v1 import app_v1
from flask import render_template

@app_v1.route('/home')
def home_page():
    return render_template('home.html')


@app_v1.route('/market')
def market_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": "893212299897", "price": 500},
        {"id": 2, "name": "Laptop", "barcode": "123985473165", "price": 900},
        {"id": 3, "name": "Keyboard", "barcode": "231985128446", "price": 150},
    ]
    return render_template("market.html", items=items)

    
