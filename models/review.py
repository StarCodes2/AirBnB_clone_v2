#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information
    Inherits from SQLAlchemy Base

    Attribute:
       __tablename__ (str): Name of the MySQL table to store Reviews.
       place_id (sqlalchemy String): Review's place id.
       user_id (sqlalchemy String): Review's user id.
       text (sqlalchemy String): Review description.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
