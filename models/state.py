#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            'City',
            cascade="all, delete-orphan",
            backref="state")
    else:
        @property
        def cities(self):
            """"""
            from models import storage
            list_cities = []
            for item in storage.all(City).values():
                if item.state_id == self.id:
                    list_cities.append(item)
            return list_cities
