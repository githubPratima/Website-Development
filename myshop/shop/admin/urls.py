
from flask import render_template, session, request, redirect, url_for,flash, Response

from flask_login import current_user, login_fresh, login_required, login_user, logout_user

from shop import app, db,bcrypt, login_manager, products
from shop.products.models import Category, Product
from .forms import AddUserForm, RegistrationForm, LoginForm
from .models import Roles, User


def chechAuth():
    try:
        if current_user:
            return True
    except:
        return False

@login_manager.user_loader
def load_user(user_id):

    
    return User.query.get(int(user_id))



@app.route('/')
def admin():
    session.permanent = False
    print(app.secret_key)
    category = Category.query.all()
    products = Product.query.filter_by(visibility = True).all()
    return render_template('admin/index.html', title="Admin", products = products, categories = category)

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username = form.username.data, 
                    email = form.email.data,
                    password = hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.username.data}! Thank you for registering', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="My Shop - Registeration")

@app.route('/login', methods=['GET', 'POST'])
def login():
    resp = Response()
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            session.permanent = False
            flash(f'Welcom back {form.email.data}! you are logged in', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            if user:
                flash('Worng password. Please try again', 'danger')
            else:
                flash('Username or email doesnot exist', 'danger')
    return render_template('admin/login.html', form=form, title='Login Page')

@app.route('/check_username', methods=['POST'])
def check_username():
    try:
        username = request.form['username']

        user = User.query.filter_by(username = username).first()

        if user:
            return "taken"
        else:
            return "not taken"
    except Exception as e:
        print(e)

@app.route('/check_email', methods=['POST'])
def check_email_user():
    try:
        email = request.form['email']

        user = User.query.filter_by(email = email).first()
        print(user)
        if user:
            return "taken"
        else:
            return "not taken"
    except Exception as e:
        print(e)

@app.route('/logout')
def logout():
    logout_user()
    resp = Response()
    resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    session.pop('cart', None)

    flash("logout is successfull", 'success')
    
    return redirect(request.args.get('next') or url_for('admin'))


@login_required
@app.route('/addUser', methods=['GET', 'POST'])
def addUser():
    form = AddUserForm(request.form)
    if request.method == 'POST':
        hash_password = bcrypt.generate_password_hash(form.password.data)
        role = form.role.data
        if role == 'Roles.generic_user':
            role = Roles.generic_user
        elif role == 'Roles.retail_user':
            role = Roles.retail_user
        else:
            role = Roles.site_manager
        user = User(username = form.username.data, 
                    email = form.email.data,
                    password = hash_password,
                    role = role
                    )
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data} user is registered!', 'success')
        return redirect(url_for('dashboard'))
        
    return render_template('admin/addUser.html', title="Add User", form=form)

@login_required
@app.route('/adminEditUser/<id>')
def adminEditUser(id):
    form = AddUserForm(request.form)
    user = User.query.get(id) 
    if user and request.method == 'POST':
        pass
    form.username.data = user.username 
    form.email.data = user.email 
    form.role.data = str(user.role)
    

    return render_template('admin/editUser.html', title="Edit User", form = form)