#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'), nullable=False,
                                 primary_key=True),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'), nullable=False,
                                 primary_key=True))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """"""
            list_reviews = []
            for item in self.reviews:
                if item.place_id == self.id:
                    list_reviews.append(item)
            return list_reviews

        @property
        def amenities(self):
            """establishes many to many relationship b/w ... """
            list_amenities = []
            for le_id in amenity_ids:
                key = 'Amenity.' + str(le_id)
                if FileStorage.__objects[key]:
                    list_amenities.append(FileStorage.__objects[key])
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """ setter to add Amenity.id to amenity_ids """
            if isinstance(value, Amenity):
                ameninty_ids.append(value.id)
