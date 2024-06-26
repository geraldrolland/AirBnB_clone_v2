#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv


class DBStorage:
    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
    metadata = MetaData()
    metadata.reflect(bind=engine)
    metadata.drop_all(bind=engine)
