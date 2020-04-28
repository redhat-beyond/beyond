#!/usr/bin/env python

from flask import render_template, flash, redirect, url_for, send_from_directory
from baboon import app, db, bcrypt
from baboon.forms import RegistrationForm
from baboon.models import Users
import os


@app.route('/')
def index():
    return render_template('/home.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('/register.html', form=form)
