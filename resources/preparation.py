"""
Use this script to prepare the postgresql service for its upcoming tasks.
"""

from sqlalchemy.schema import CreateSchema
from sqlalchemy_utils import create_database, database_exists

from garden.config.target import SCHEMA
from garden.database.base import Base, Engine

if __name__ == "__main__":
    if not database_exists(Engine.url):
        create_database(Engine.url)

    if not Engine.dialect.has_schema(Engine, SCHEMA):
        Engine.execute(CreateSchema(SCHEMA))

    Base.metadata.create_all(Engine)
