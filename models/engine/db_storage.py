#!/usr/bin/python3
"""DB Storage to save in MySQL
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        NewDict = {}
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session(self.__engine)
        if cls is None:
            query_objs = self.__session.query(User, State,
                                              City, Amenity,
                                              Place, Review).all()
            if query_objs is None:
                return {}
            for obj in query_objs:
                key_obj = ("{}.{}".format(obj.__class__.__name__, obj.id))
                NewDict[key_obj] = obj
            return NewDict
        else:
            query = self.__session.query(self.__class__.__name__).all()
            if query is None:
                return {}

            for key, value in self.NewDict.items():
                    if cls == value.__class__:
                        _instance[key] = value
            return NewDict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()