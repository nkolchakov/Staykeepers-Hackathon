from models import *
from server import db

def getListings():
    listings = Listing.query.all()
    for listing in listings:
        print(listing)

    return listings

def getListingById(id):
    listing = Listing.query.filter_by(id=id).first()
    print(listing)

    return listing