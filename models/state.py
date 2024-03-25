#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class
    Inherits from SQLAlchemy Base and links to the MySql table states.

    Attributes:
       __tablename__ (str): Name of the MySQL table to store States objects.
       name (sqlalchemy String): Name of the state.
       cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        import models

        @property
        def cities(self):
            """ Returns a list of all related City obects. """
            city_list = []
            for city in list(models.storage.all(city).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
