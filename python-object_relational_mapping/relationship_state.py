#!/usr/bin/python3
"""Defines the State model with a cities relationship."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """A US state; deleting it deletes its linked cities."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", order_by="City.id",
                          cascade="all, delete-orphan")
