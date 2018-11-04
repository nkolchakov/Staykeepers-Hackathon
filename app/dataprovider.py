from models import *
import requests
import json

def getListings():
    listings = Listing.query.all()

    listingsDto = [listingToDto(listing, False) for listing in listings]
    return listingsDto

def getListingById(id):
    listing = Listing.query.filter_by(id=id).first()

    dto = listingToDto(listing)
    return dto



def listingToDto(listing, checkLandmarks = True):
    imgs = [img.image_path  for img in  listing.images] * 3

    lat = float(listing.latitude);
    lng = float(listing.longitude);

    username = ''
    if listing.user is None:
        username = 'default'
    else:
        username = listing.user.username

    landmarks = [{ "lat": 42.698334, "lng": 23.319941, "title": "Hi" }];

    if checkLandmarks:
        print('checking landmarks ...')
        landmarks = getLandmarks(lat, lng)
    else:
        print('skipping landmars ...')

    dto = {
        "id": listing.id,
        "guests": listing.guests,
        "baths": listing.baths,
        "title": listing.address,
        "price": listing.price,
        "landmarks": landmarks,
        "landmarksCount": len(landmarks),   
        "lat": lat,
        "lng": lng,
        "rating": listing.rating,
        "user": {"name": username},
        "images": imgs,
        "amenities": listing.amenities,
        "description": listing.description
    }

    return dto


def getLandmarks(lat, lng):
    
    defaultLocation = {
        "lat": 42.698334, 
        "lng": 23.319941
    };

    appId = 'wgV16NBsDKmQocrusbbq'
    appCode = 'ZZOvDZwcmhoKQ-ZqFHmtZg'

    url = "https://reverse.geocoder.api.here.com/6.2/reversegeocode.json?app_id=%s&app_code=%s&mode=retrieveLandmarks&prox=%s,%s,1000" % (appId, appCode, lat, lng)

    r = requests.get(url)
    dictData = r.json()

    resultsList = dictData["Response"]["View"] 
    results = []
    if len(resultsList) > 0:
        print 
        results = resultsList[0]["Result"];
    else:
        return []

    r = []

    for res in results:
        lat = res["Location"]["DisplayPosition"]["Latitude"]
        lng = res["Location"]["DisplayPosition"]["Longitude"]
        title = res["Location"]["Name"]
        locationType = res["Location"]["LocationType"]

        mapped = {
            'lat': lat, 
            'lng': lng, 
            'title': title, 
            'locationType': locationType  
        }
        print(mapped)
        r.append(mapped)
    return r