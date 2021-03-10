#!/usr/bin/env python
from flask import render_template
from beyond import app


@app.route('/')
def index():
    return render_template('/home.html')


@app.route('/contacts')
def contacts():
    return render_template('/contacts.html')


@app.route('/cycles')
def cycles():
    return render_template('/cycles.html')
