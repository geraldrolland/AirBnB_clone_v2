#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        if os.getenv("HBNB_TYPE_STORAGE") == FileStorage:
            all_city_obj = storage.all(City)
            city_list = []
            for city in all_city_obj:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
