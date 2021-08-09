"""
This module holds the greenhouse class.
This class represents the greenhouse table inside the target database.
"""

__all__ = [
    "Greenhouse",
]

from greenhouse.config.target import SCHEMA
from greenhouse.database.base import Base
from sqlalchemy import Column, Float, Integer, String


class Greenhouse(Base):
    __tablename__ = "greenhouse"
    __table_args__ = {"schema": SCHEMA}

    id = Column(Integer, primary_key=True)
    timestamp = Column(String, nullable=False)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    moisture = Column(Float, nullable=True)
    sun_intensity = Column(Float, nullable=True)

    def __init__(
        self,
        timestamp,
        temperature,
        humidity,
        moisture,
        sun_intensity,
    ):
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.moisture = moisture
        self.sun_intensity = sun_intensity