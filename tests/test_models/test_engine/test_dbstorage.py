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
from models.amenity import Amenity
from models import storage
import models
import os
import unittest


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "testing db storage")
class test_DBStorage(unittest.TestCase):

    def testCity(self):
        city = City(name="Philadelphia")
        if city.id in storage.all():
            self.assertTrue(city.name, "Philadelphia")

    def testPlace(self):
        place = Place(name="pad")
        if place.id in storage.all():
            self.assertTrue(place.name, "pad")

    def testReview(self):
        review = Review(text="this place stinks")
        if review.id in storage.all():
            self.assertTrue(review.text, "this place stinks")

    def testState(self):
        state = State(name="Mississippi")
        if state.id in storage.all():
            self.assertTrue(state.name, "Mississippi")

    def testUser(self):
        user = User(first_name="Jimmy")
        if user.id in storage.all():
            self.assertTrue(user.first_name, "Jimmy")

    def testAmenity(self):
        amenity = Amenity(name="towels")
        if amenity.id in storage.all():
            self.assertTrue(amenity.name, "towels")
