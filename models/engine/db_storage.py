#!/usr/bin/python3
"""New engine"""
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
import os

user=os.getenv("HBNB_MYSQL_USER")
password=os.getenv("HBNB_MYSQL_PWD")
host=os.getenv("HBNB_MYSQL_HOST")
database=os.getenv("HBNB_MYSQL_DB")

__engine = None
__session = None

class DBStorage:
    """engine class"""
    def __init__(self):
        """create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)
    def all(self, cls=None):
        """"""
        db_dict = {}
        if cls:
            print("Hello")
            for key, value in classes.items():
                if key == cls.__name__:
                    for item in self.__session.query(cls.__name__).all():
                        key = "{}.{}".format(cls.__name__, item.id)
                        db_dict[key] = item
        else:
            print("to more")
            for k, value in classes.items():
                for item in self.__session.query(value).all():
                    key = "{}.{}".format(k, item.id)
                    db_dict[key] = item
    def new(self, obj):
        """'"""
        if obj:
            self.__session.add(obj)
            self.__session.commit()

    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """"""
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


