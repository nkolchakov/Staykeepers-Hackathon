from faker import Faker
from server import db
from models import *

pathImages = [
    '../static/imgs/1.png',
    '../static/imgs/2.png',
    '../static/imgs/3.png',
    '../static/imgs/4.png'
]

fake = Faker()

# add event
# add image
# add amedity
def createListing():
    listing = Listing(
        price = fake.random_int(min=0, max=10000),
        address = fake.street_address(),
        latitude =  str(fake.latitude()),
        longitude = str(fake.longitude()),
        rating = fake.random_int(min=0, max=4),
        createdDate = fake.date_this_decade(),
        description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
        guests = fake.random_int(min=1, max=4),
        bedrooms = fake.random_int(min=1, max=5),
        beds = fake.random_int(min=1, max=5),
        baths = fake.random_int(min=1, max=3),
        isDeleted = 0
    )
    return listing

def createEvent():
    event = Event(
        title = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
        createdDate = fake.date_this_decade(),
    )

    return event

def createImage():
    randomIndex = fake.random_int(min=0, max=(len(pathImages) - 1));
    image = Image(
        image_path = pathImages[randomIndex]
    )
    return image

def createAmenity():
    amenity = Amenity(
        goody_title = fake.word(ext_word_list=None)
    )
    return amenity

# add listing, image
def createUser():
    user = User(
                username = fake.word(ext_word_list=None),
                email = fake.email(),
                password = User.encrypt_password('asd123'),
    )
    return user


user = createUser()

db.session.add(user)

listing = createListing()
listing.images = [createImage() for i in range(0,5)]

listing2 = createListing()
listing2.images = [createImage() for i in range(0,5)]

print(listing.isDeleted)

db.session.add(listing)
db.session.add(listing2)

db.session.commit()

user.listings.append(listing)
user.listings.append(listing2)
user.image_path.append(createImage())

listing.events.append(createEvent())
listing.events.append(createEvent())
listing2.events.append(createEvent())

listing.images.append(createImage())
listing.images.append(createImage())
listing2.images.append(createImage())

# db.session.commit()