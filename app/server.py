from flask import Flask, render_template, jsonify
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
import json

# Create the application instance
app = Flask(__name__, template_folder="templates")
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///winwin.sqlite3'

db = SQLAlchemy(app)

from models import *

@app.route('/')
def home():
    return 'Hi'

@app.route('/katze')
def katze():
    k = Kotka("kotka",12)
    return jsonify(k.__dict__)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)