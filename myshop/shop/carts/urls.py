from flask import redirect, render_template, session, url_for, request
from flask_login import login_required

from shop import app, db
from shop.products.models import Product 


@app.route('/cart')
@login_required
def show_cart():
    return render_template('carts/cart.html', title="My Shop - Cart",   )

@app.route('/checkout')
@login_required
def checkout():
    return render_template('carts/checkout.html', title="My Shop - Checkout")

@app.route('/payment')
@login_required
def payment():

    return render_template('carts/payment.html', title= "My Shop - Payment")

@app.route('/add_cart', methods=['POST'])
def  add_cart():
    try:
        product_id = request.form.get('product_id')
        print(product_id)
        quantity = int(request.form.get('qty_input'))
        print(quantity)
        product = Product.query.get(product_id)
        print(product)
        if request.method == 'POST':
            DictItems = {product_id:{'name': product.title, 'price': product.price, 'quantity':quantity }}
            print(DictItems)
            if 'cart' in session:
                print(session['cart'])
                return redirect(request.referrer)
            else:
                session['cart'] = DictItems
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)
            
    



    