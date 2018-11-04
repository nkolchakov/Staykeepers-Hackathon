from models import *
import parser


def getListings():
    listings = Listing.query.all()
    for l in listings:
        print(l.user)
    listingsDto = [listingToDto(listing) for listing in listings]
    return listingsDto

def getListingById(id):
    listing = Listing.query.filter_by(id=id).first()

    dto = listingToDto(listing)
    return dto



def listingToDto(listing):
    imgs = [img.image_path  for img in  listing.images] * 3

    lat = float(listing.latitude);
    lon = float(listing.longitude);

    username = ''
    if listing.user is None:
        username = 'default'
    else:
        username = listing.user.username

    dto = {
        "id": listing.id,
        "guests": listing.guests,
        "baths": listing.baths,
        "title": listing.address,
        "price": listing.price,
        "landmarks": [{ "lat": -80.3888495, "lng": -100.445735, "title": "Hi" }],
        "lat": lat,
        "lng": lon,
        "rating": listing.rating,
        "user": {"name": username},
        "images": imgs,
        "amenities": listing.amenities,
        "description": listing.description
    }

    return dto