from server import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    # Images
    image_path = db.relationship('Image', backref='user')

    # Many Listings
    listings = db.relationship('Listing', backref='user')
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Listing(db.Model):
    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float, nullable = False)
    address = db.Column(db.String(300), nullable = False)
    longitude = db.Column(db.String(50), nullable = True)
    rating = db.Column(db.Float, nullable = False)

    # User FK
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Many Events
    events = db.relationship('Event', backref='listing')

    # Many Images
    images = db.relationship('Image', backref='listing')

    # Many Amedities
    amedities = db.relationship('Amedity', backref='listing')

    createdDate = db.Column(db.Date, nullable = False)
    description = db.Column(db.String(350), nullable = False)
    isDeleted = db.Column(db.Integer, nullable = False)
    guests = db.Column(db.Integer, nullable = False)
    bedrooms = db.Column(db.Integer, nullable = False)
    beds = db.Column(db.Integer, nullable = False)
    baths = db.Column(db.Integer, nullable = False)

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable = False)
    createdDate = db.Column(db.Date, nullable = False)

    #Listing FK
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

class Image(db.Model):
    __tablename__ = 'images'
    
    id = db.Column(db.Integer, primary_key = True)
    image_path = db.Column(db.String(350), nullable = False)
    # FK User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # FK Listing
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key = True)
    
    # Listing FK
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

    goody_title = db.Column(db.String(200), nullable = False)

