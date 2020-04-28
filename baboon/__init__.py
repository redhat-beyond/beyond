from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '95bf1f8a8102200167b9bcf6b9cc719c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/baboon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from baboon import routes

