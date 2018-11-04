from flask import Flask, render_template, jsonify, request
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

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
    user = request.form['user']
    guests = request.form['guests']
    # image = request.form['image']

    print(request.files)
    print(request.form)

    return jsonify()


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)


mockListing = {
   "id": randint(1,10),
   "guests": 6,
   "baths": 4,
  "title": "test",
  "price": 44.5,
  "landmarks": [{ "lat": -80.3888495, "lng": -100.445735, "title": "Hi" }],
  "lat": 42.6977,
  "lng": 23.3219,
  "rating": 2.8,
  "user": { "name": "name" },
  "images": ["../static/imgs/1.png", "../static/imgs/2.png", "../static/imgs/3.png", "../static/imgs/4.png","../static/imgs/1.png", "../static/imgs/2.png", "../static/imgs/3.png", "../static/imgs/4.png"],
  "amenities": ["test", "test1", "test2", "test3", "test4"],
  "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas justo dolor, interdum quis sodales ut, viverra ut nisl. In tempor sit amet quam non rhoncus. Suspendisse potenti. Cras convallis interdum arcu, eu tincidunt metus lacinia eu. Mauris eleifend pharetra tristique. Sed nisi sapien, laoreet non nunc non, faucibus mattis odio. Fusce ac sodales ex, quis lobortis neque. Ut non ex tellus. Proin tellus massa, condimentum quis dignissim sed, ornare blandit tortor. Phasellus ipsum velit, dignissim egestas metus in, lobortis gravida erat. Aenean vel dui lorem. Curabitur a velit risus. Proin ut malesuada magna. Donec nunc nisi, condimentum pharetra justo porttitor, vehicula fermentum mauris. Pellentesque scelerisque egestas egestas. Curabitur facilisis elit nibh, accumsan porttitor mauris fermentum et. Phasellus ornare molestie tortor quis pretium. Integer elementum arcu in justo efficitur placerat. Donec tincidunt iaculis ante nec dapibus. Fusce eu velit sed sem luctus convallis eu vel ipsum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam sed ante sollicitudin, vestibulum neque id, imperdiet odio. Nulla ut gravida leo. Nam vel efficitur urna. Nam nulla dui, auctor eu molestie non, rutrum sed nisl. Cras ligula nisl, ornare laoreet egestas sit amet, consequat sed lorem. Vestibulum ultrices tristique consectetur."
}