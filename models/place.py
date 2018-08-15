#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os

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
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='place')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """"""
            from models import storage
            list_reviews = []
            for item in storage.all(Review).values():
                if item.place_id == self.id:
                    list_reviews.append(item)
            return list_reviews

        @property
        def amenities(self):
            """establishes many to many relationship b/w ... """
            from models import storage
            list_amenities = []
            objs = storage.all(Amenity)
            for i in objs:
                if i.id in amenity_ids:
                    list_amenities.append(i)
            return list_amenities

        @amenities.setter
        def amenities(self, value):
            """ setter to add Amenity.id to amenity_ids """
            if isinstance(value, Amenity):
                ameninty_ids.append(value.id)
