#!/usr/bin/env python

import os

from flask import render_template, send_from_directory

from baboon import app

@app.route('/')
def index():
    return render_template('/home.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
