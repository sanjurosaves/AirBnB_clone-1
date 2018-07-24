#!/usr/bin/python3
'''
    Define class DBStorage
'''
import models
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import os

# cls_names = ["BaseModel", "User", "State", "City",
#            "Amenity", "Place", "Review"]
# consider importing from console module

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{} , pool_pre_ping=True'
            .format(os.environ['HBNB_MYSQL_USER'],
                    os.environ['HBNB_MYSQL_PWD'],
                    os.environ['HBNB_MYSQL_HOST'],
                    os.environ['HBNB_MYSQL_DB']))

# not sure about this        Base.metadata.create_all(engine)

        if (os.environ['HBNB_ENV'] == 'test'):
            drop_all(bind=self.__engine)

        self.__session = Session(self.__engine)

    def all(self, cls=None):
        __session = Session(engine)
        return_dict = {}

        if (cls):
            for obj in session.query(cls).all():
                return_dict = dict(obj)
        else:
            for cname in Base.__subclasses__:
                for obj in session.query(cls).all():
                    return_dict = dict(obj)

        return return_dict

    def new(self, obj):
        pass

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            pass

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
