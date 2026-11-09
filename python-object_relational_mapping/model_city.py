#!/usr/bin/python3
"""Defines the City model mapped to the cities table."""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """A city stored in the cities table, linked to a state."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
