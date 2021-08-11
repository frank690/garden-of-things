"""
This module holds base information and functionality to establish a
connection with the database via sqlAlchemys ORM classes.
"""

__all__ = [
    "Session",
    "Base",
    "Engine",
]

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema

from garden.config.target import DATABASE, IP, PW, SCHEMA, USER

Engine = create_engine("postgresql://{0}:{1}@{2}/{3}".format(USER, PW, IP, DATABASE))
Session = sessionmaker(bind=Engine)
Base = declarative_base()

if not Engine.dialect.has_schema(Engine, SCHEMA):
    Engine.execute(CreateSchema(SCHEMA))
