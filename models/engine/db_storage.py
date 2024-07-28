#!/usr/bin/python3

from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import Base
from models.amenity import Amenity
from sqlalchemy import create_engine, MetaData


class DBStorage:
    __session = None
    __engine = None

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        metadata = MetaData()
        metadata.reflect(bind=self.__engine)
        metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        obj_dict = {}
        if cls is not None:
            obj_list = self.__session.query(cls).all()
            for obj in obj_list:
                key = obj.__class__.__name__ + "." + str(obj.id)
                obj_dict.update({key: obj})
            self.__session.close()
            return obj_dict
        for cl in [User, State, City, Amenity, Place, Review]:
            all_obj_list = self.__session.query(cl).all()
            for obj in all_obj_list:
                key = obj.__class__.__name__ + "." + str(obj.id)
                obj_dict.update({key: obj})
        self.__session.close()
        return obj_dict

    def new(self, obj):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        self.__session.add(obj)

    def save(self):
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        if obj is not None:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            obj = self.__session.query(type(obj)).filter(type(obj).id == obj.id).one_or_none()
            if obj is not None:
                self.__session.delete(obj)
                self.__session.commit()
            self.__session.close()

    def reload(self):
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        Base.metadata.create_all(bind=self.__engine)
        self.__session.close()

    def close(self):
        self.__session.remove()
