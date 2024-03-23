#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name
        Inherits from SQLAlchemy Base and links to the MySQL table cities.

        Attributes:
            __tablename__ (str): Name of the table to store cities
            state_id (sqlalchemy String): State_id of the city.
            name (sqlalchemy String): Name of the city
    """
    state_id = Column(String(128), nullable=False)
    name = Column(String(60), ForeignKey("state.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
