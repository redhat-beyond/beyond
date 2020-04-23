#!/usr/bin/env python

import os
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('/home.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
