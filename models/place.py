#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        if getenv('HBNB_TYPE_STORAGE') != 'db':
            @property
            def reviews(self):
                """getter attribute cities to returns the list of City instances"""
                from models import storage
                from models.review import Review
                reviews = []
                for review in storage.all(Review).values():
                    if review.place_id == self.id:
                        reviews.append(review)
                return reviews

            @property
            def amenities(self):
                """getter attribute cities to returns the list of City instances"""
                from models import storage
                from models.amenity import Amenity
                amenities = []
                for amenity in storage.all(Amenity).values():
                    if amenity.id in self.amenity_ids:
                        amenities.append(amenity)
                return amenities

            @amenities.setter
            def amenities(self, obj):
                """setter attribute cities to returns the list of City instances"""
                if type(obj).__name__ == 'Amenity':
                    self.amenity_ids.append(obj.id)
