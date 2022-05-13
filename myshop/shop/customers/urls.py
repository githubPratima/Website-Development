from turtle import title
from flask import flash, render_template, request,redirect, url_for
from flask_login import current_user, login_required

from shop.admin.urls import chechAuth
from shop import app, db, bcrypt
from shop.products.models import Product
from .forms import UpdateUserForm 
from shop.admin.models import Roles, User


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = UpdateUserForm(request.form)
    if request.method == 'POST' and form.validate():

        return redirect(url_for('login'))
    return render_template('customer/settings.html',form =form ,title= "My Shop-Settings")

@app.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.filter_by(brand_id = current_user.id).all()
    users = User.query.all()
    return render_template('customer/dashboard.html', title="My Shop - Dashboard", products=products, users=users)

@app.route('/dashboard/add_product')
@login_required
def add_product():
    return render_template('customer/dashboard.html', title= "My Shop - Add Product")

@app.route('/dashboard/users')
@login_required
def get_all_users():
    return render_template('customer/usersList.html', title="My Shop - Users List")



#curd operations
@app.route('/update-user', methods=['POST'])
def updateUser():
    id = current_user.id 
    form = UpdateUserForm(request.form)
    user = User.query.get(id)
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        user.username = form.username.data
        user.email = form.email.data
        db.session.commit()
        flash('Succefully changed your profile', 'success')
        return redirect(request.args.get('next') or url_for('admin'))
    else:
        flash('Worng password. Please try again', 'danger')
        return redirect(url_for('settings'))

@app.route('/update-pwd', methods=['POST'])
def updatePwd():
    id = current_user.id 
    form = UpdateUserForm(request.form)
    user = User.query.get(id)
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        hash_password = bcrypt.generate_password_hash(form.new_pwd.data)
        user.password = hash_password
        db.session.commit()
        return redirect(request.args.get('next') or url_for('admin'))
    else:
        flash('Worng password. Please try again', 'danger')
        return redirect(url_for('settings'))
    

@app.route('/delete-user/<id>')
def deleteUser(id): 
    user = User.query.get(id) 
    try:
        db.session.delete(user)
        db.session.commit()
        flash('user is deleted', 'success')
        return redirect(url_for('dashboard'))
    except:
        flash('error in deleting order, please try again', 'danger')
        return redirect(url_for('dashboard'))
    


@app.route('/change_reatiler/<id>')
def retailchange(id):
    user  = User.query.get(id)
    if user.role == Roles.retail_user:
        flash('you are already a reatil user', 'success')
        return redirect(url_for('admin'))
    try:
        user.role = Roles.retail_user
        db.session.commit()
        flash('role changed successfully!', 'success')
        return redirect(url_for('admin'))
    except:
        flash('unable to change roles, please try again later!', 'danger')
        return redirect(url_for('admin'))

