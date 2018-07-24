#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.base_model import Base
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete-orphan", backref="state")
    else:
        name = ""
