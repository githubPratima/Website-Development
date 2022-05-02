from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'milk',  'price': 2},
        {'id': 2, 'name': 'sausage',  'price': 5},
        {'id': 3, 'name': 'egg',  'price': 3},
        {'id': 4, 'name': 'bread', 'price': 5},
        {'id': 5, 'name': 'detergent', 'price': 8},
        {'id': 6, 'name': 'pasta', 'price': 3},
        {'id': 7, 'name': 'chocholate', 'price': 4},
        {'id': 8, 'name': 'salt', 'price': 5},
        {'id': 9, 'name': 'organic_rice', 'price': 10},
        {'id': 10, 'name': 'butter', 'price': 7},
    ]
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run()