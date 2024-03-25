#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
    Inherits from SQLAlchemy Base and links to the MySQL table places.

    Attributes:
        __tablename__ (str): Name of the MySQL table to store places.
        city_id (sqlalchemy String): Place's city id.
        user_id (sqlalchemy String): Place's user id.
        name (sqlalchemy String): Place name.
        description (sqlalchemy String): Place description.
        number_rooms (sqlalchemy Integer): Number of rooms.
        number_bathrooms (sqlalchemy Integer): Number of bathrooms.
        max_guest (sqlalchemy Integer): Maximum number of guests.
        price_by_night (sqlalchemy Integer): Price by night.
        latitude (sqlalchemy Float): Place's latitude.
        longitude (sqlalchemy Float): Place's longitude.
        reviews (sqlalchemy relationship): Place-Review relationship.
        amenities (sqlalchemy relationship): Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """ Get a list of all Reviews for a place. """
            rev_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    rev_list.append(review)
            return rev_list

        @property
        def amenities(self):
            """ Get a list of all Amenities for a place. """
            ame_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    ame_list.append(amenity)
            return ame_list

        @amenities.setter
        def amenities(self, value):
            """ Set a new Amenity to a place. """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
