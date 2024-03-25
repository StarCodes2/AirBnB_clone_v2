#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ This class defines a user by various attributes
    Inherits from SQLAlchemy BaseModel and Base

    Attributes:
       __tablename__ (str): Name of the table states.
       email (sqlalchemy String): User's email
       password (sqlalchemy String): User's password
       first_name (sqlalchemy String): User's first name
       last_name (sqlalchemy String): User's last name
       places (sqlalchemy relationship): User-Place relationship
       reviews (sqlalchemy relationship): User-Review relationship
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
