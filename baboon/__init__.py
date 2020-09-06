from flask import Flask

app = Flask(__name__)

# flake8: noqa
from baboon import routes
