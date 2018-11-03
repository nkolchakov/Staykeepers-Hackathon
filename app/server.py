from flask import Flask, render_template, jsonify
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

import json

# Create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///winwin.sqlite3'


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from models import *

@app.route('/')
def home():
    return '( ͡° ͜ʖ ͡°)  Hii'

@app.route('/katze')
def katze():
    return 'Kotka'

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)