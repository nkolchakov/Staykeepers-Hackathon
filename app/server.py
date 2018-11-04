from flask import Flask, render_template, jsonify, request
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from werkzeug.datastructures import ImmutableMultiDict

from random import randint

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
def details():
    id = request.args.get('id')
    listingDto = dataprovider.getListingById(id)
    return render_template('listing.html', listing = listingDto )

@app.route('/')
def allListings():
    listingsDto = dataprovider.getListings()
    return render_template('listings.html', listings = listingsDto)


@app.route('/createListing')
def createListing():
    return render_template('create-listing.html')

# ImmutableMultiDict([('user', 'asdas'), ('price', '12'), ('guests', '1'), 
# ('bedrooms', '1'), ('beds', '1'), ('baths', '1'),
#  ('amenities', ''), ('description', '')])
@app.route('/createListing', methods=['POST'])
def create():
    d = request.form.to_dict(flat=False)

    dataprovider.createListing(d)

    print(d)

    return jsonify()


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
