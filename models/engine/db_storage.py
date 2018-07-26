#!/usr/bin/python3
"""New engine"""
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models
import os

user = os.getenv("HBNB_MYSQL_USER")
password = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
database = os.getenv("HBNB_MYSQL_DB")

__engine = None
__session = None


class DBStorage:
    """engine class"""

    def __init__(self):
        """create the engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, password, host, database), pool_pre_ping=True, echo=True)
        Base.metadata.create_all(self.__engine)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """"""
        db_dict = {}
        if cls:
            #            print("Hello")
            if cls.__name__ in temp_cls:
                for item in self.__session.query(cls).all():
                    key = "{}.{}".format(cls.__name__, item.id)
                    db_dict[key] = item
        else:
            #            print("to more")
            for k, value in models.temp_cls.items():
                for item in self.__session.query(value).all():
                    key = "{}.{}".format(k, item.id)
                    db_dict[key] = item
        return db_dict

    def new(self, obj):
        """'"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """"""
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
