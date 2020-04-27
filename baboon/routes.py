#!/usr/bin/env python

from flask import render_template, flash, redirect, url_for, send_from_directory
import os
from baboon import app


@app.route('/')
def index():
    return render_template('/home.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
