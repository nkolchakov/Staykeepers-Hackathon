from server import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String())

    # Images
    image_path = db.relationship('Image', backref='user')

    # Many Listings
    listings = db.relationship('Listing', backref='user')
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @staticmethod
    def encrypt_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def is_correct_password(self, plaintext):
        if bcrypt.check_password_hash(self.password, plaintext):
            return True
        return False

    def save(self):
        db.session.add(self)
        db.session.commit()

class Listing(db.Model):
    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float, nullable = False)
    address = db.Column(db.String(300), nullable = False)
    latitude = db.Column(db.String(50), nullable = True)
    longitude = db.Column(db.String(50), nullable = True)
    rating = db.Column(db.Float, nullable = False)

    # User FK
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Many Events
    events = db.relationship('Event', backref='listing')

    # Many Images
    images = db.relationship('Image', backref='listing')

    # Many amentities
    amenities = db.relationship('Amenity', backref='listing')

    createdDate = db.Column(db.Date, nullable = False)
    description = db.Column(db.String(350), nullable = False)
    isDeleted = db.Column(db.Integer, nullable = False)
    guests = db.Column(db.Integer, nullable = False)
    bedrooms = db.Column(db.Integer, nullable = False)
    beds = db.Column(db.Integer, nullable = False)
    baths = db.Column(db.Integer, nullable = False)

    def __int__(self, price, address, lat, lon, rating, createdDate, descr, guests, bedrooms, beds, baths):
        self.price = price
        self.address =address
        self.latitude = lat
        self.longitude = lon
        self.rating = rating
        self.createdDate = createdDate
        self.description = descr
        self.isDeleted = 0
        self.guests = guests
        self.bedrooms = bedrooms
        self.beds = beds,
        self.baths = baths
    

    def save(self):
        db.session.add(self)
        db.session.commit()


class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), nullable = False)
    createdDate = db.Column(db.Date, nullable = False)

    #Listing FK
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

    def __init__(self, title, createdDate):
        self.title = title
        self.createdDate = createdDate

    def save(self):
        db.session.add(self)
        db.session.commit()

class Image(db.Model):
    __tablename__ = 'images'
    
    id = db.Column(db.Integer, primary_key = True)
    image_path = db.Column(db.String(350), nullable = False)
    # FK User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # FK Listing
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

    def __init__(self, image_path):
        self.image_path = image_path

    def save(self):
        db.session.add(self)
        db.session.commit()


class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key = True)
    goody_title = db.Column(db.String(200), nullable = False)
    
    # Listing FK
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))

    def __init__(self, goody_title):
        self.goody_title = goody_title

    def save(self):
        db.session.add(self)
        db.session.commit()