"""
This module holds base information and functionality to establish a
connection with the database via sqlAlchemys ORM classes.
"""

__all__ = [
    "Session",
    "Base",
]

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from garden.config.target import DATABASE, IP, PW, USER

Engine = create_engine("postgresql://{0}:{1}@{2}/{3}".format(USER, PW, IP, DATABASE))
Session = sessionmaker(bind=Engine)
Base = declarative_base()
