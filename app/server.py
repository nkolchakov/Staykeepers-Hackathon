from flask import Flask, render_template, jsonify, request
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

import dataprovider
from models import *

@app.route('/listing')
def home():
    id = request.args.get('id')
    listing = dataprovider.getListingById(id)

    return jsonify(listing.address)

    return render_template('listing.html', listing = { "landmarks": [{"lat":-80.3888495 , "lng": -100.445735, "title": "Hi"}], "lat":-80.3888495 , "lng": -100.445735, "user":{"name":"name"}, "images":["../static/imgs/1.png","../static/imgs/2.png"]})

@app.route('/katze')
def katze():
    return 'Kotka'

@app.route('/listings')
def listings():
    listings = dataprovider.getListings()
    return jsonify(len(listings))



# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)