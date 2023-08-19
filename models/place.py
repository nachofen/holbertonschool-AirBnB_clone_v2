#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """getter attribute reviews that returns the list of Review instances
            with place_id equals to the current Place.id"""
            from models.review import Review
            from models import storage
            list_reviews = []
            for review in storage.all(Review).values():
                if self.id == review.place_id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """getter attribute amenities that returns the list of Amenity
            instances with place_id equals to the current Amenity.id"""
            from models.amenity import Amenity
            from models import storage
            list_amenities = []
            for amenity in storage.all(Amenity).values():
                if self.id == amenity.place_id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """setter attribute for amenities that appends an Amenity instance
            to the list of amenities."""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)