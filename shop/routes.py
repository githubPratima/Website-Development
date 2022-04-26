from flask import Flask, session, render_template, redirect, request, flash
from shop import app, db
from flask_sqlalchemy import SQLAlchemy
from .form import RegistationForm

@app.route('/')
def home():
   return "shop homepage"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
       # user = User(form.username.data, form.email.data,
                   # form.password.data)
        #db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title= "Registration Page")


if __name__ == "__main__":
   app.run()