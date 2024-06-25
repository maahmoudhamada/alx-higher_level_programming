#!/usr/bin/python3
"""The model_state module"""


import sys
import sqlalchemy
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """State class represent db table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
