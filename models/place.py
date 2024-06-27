#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
import os

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1028))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade="all, delete-orphan", backref="place")
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                viewonly=False
            )
    else:
        @property
        def amenities(self):
            from models import storage
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get(Amenity, amenity_id)
                if amenity:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(amenity, Amenity):
                if amenity.id not in self.amenity_ids:
                    self.amenity_ids.append(amenity.id)

    @property
    def reviews(self):
        """Returns a list of review object that has the same place_id with place object"""
        from models import storage
        from models.review import Review
        all_review_obj = []
        all_obj_dict = storage.all(Review)
        for obj in all_obj_dict.values():
            if obj.place_id == self.id:
                all_review_obj.append(obj)
        return all_review_obj

