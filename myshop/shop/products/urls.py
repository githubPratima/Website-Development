from datetime import datetime
from itertools import product

from flask import redirect, render_template, url_for, flash, request
from flask_login import current_user, login_required
from requests import session
from sqlalchemy import desc
from shop import db, app
from shop.products.models import Brand, Category, Product
from .forms import AddProductsForm 

@login_required
@app.route('/addproduct', methods=['GET', 'POST'])
def addProduct():
    
    form  =  AddProductsForm(request.form)
    if request.method == "POST":
        brand = Brand.query.filter_by(name = current_user.username).first()
        if  not brand:
            brand = Brand(
                name = current_user.username,
                user_id = current_user.id,
            )
            db.session.add(brand)
            db.session.commit()
        cat = Category.query.filter_by(name = form.category.data).first()
        if not cat:
            cat = Category(
                name = form.category.data,
            )
            db.session.add(cat)
            db.session.commit()
        product = Product(
            title = form.name.data,
            brand_id = brand.id,
            category_id = cat.id,
            price = form.price.data,
            stock = form.stock.data,
            desc = form.description.data,
            last_modified = datetime.utcnow(),
            visibility = form.visibility.data,
            
        )
        
        
        db.session.add(product)
        db.session.commit()
        flash('product added', 'success')
        return redirect(url_for('admin'))

    return render_template('products/addProduct.html', title="Add product", form = form)

@app.route('/product/<id>')
def singlePage(id):
    product = Product.query.get(id)

    return render_template('products/singlePage.html', title="Detailed page", product = product)

@app.route('/edit_product/<id>', methods=['GET', 'POST'])
def edit_product(id):
    form  =  AddProductsForm(request.form)
    product = Product.query.get(id)
    if product and request.method == 'POST':
        cat = Category.query.filter_by(name = form.category.data).first()
        if not cat:
            cat = Category(
                name = form.category.data,
            )
            db.session.add(cat)
            db.session.commit()  

        product.title = form.name.data
        product.category_id = cat.id
        product.price = form.price.data
        print(product.price)
        print(form.price.data)
        product.stock = form.stock.data
        product.desc = form.description.data
        product.last_modified = datetime.utcnow()
        product.visibility = form.visibility.data
        
        try:
            
            db.session.commit()
            flash("Product successfully changed!", 'success')
            return redirect(url_for('dashboard'))
        except Exception as e :
            print(e)
            flash('error editing product. Please try again later', 'danger')
            return redirect(url_for('dashboard'))

    form.name.data = product.title
    form.category.data = product.category.name
    form.price.data = int(product.price)
    form.stock.data = product.stock
    form.description.data = product.desc
    # datetime.utcnow()
    form.visibility.data = product.visibility
    
    

    return render_template('products/editProduct.html', title="Edit Product", form = form, product=product)

@app.route('/deleteProduct/<id>')
def deleteProduct(id):
    product = Product.query.get(id)
    try:
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        flash('product deleted', 'success')
        return redirect(url_for('dashboard'))
    except:
        flash('error in deleting product, please try again', 'danger')
        return redirect(url_for('dashboard'))
