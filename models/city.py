#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    place = relationship('Place', cascade='all, delete-orphan',
                             backref='cities')
