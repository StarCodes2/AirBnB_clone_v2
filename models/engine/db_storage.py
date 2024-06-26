#!/usr/bin/python3
""" Defines the DBStorage engine using SQLAlchemy. """
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """ Represents the database storage engine.
    Attributes
       __engine (sqlalchemy.Engine): The  SQLAlchemy engine.
       __session (sqlalchemy): The SQLAlchemy session
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize a new DBStorage instance. """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query the current database session for all objs of a given class.
        Or all objects in the database if cls is None.

        Return:
           A dictionary of objects
        """
        if cls is None:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """ Adds an obj to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes in the current session to the database. """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an obj from the current database session. """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database and initializes a new session """
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        Session = scoped_session(session_maker)
        self.__session = Session()

    def close(self):
        """ Close the current database session. """
        self.__session.close()
