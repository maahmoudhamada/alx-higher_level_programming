#!/usr/bin/python3
"""The State class module"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import sqlalchemy
import sys

data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
    .format(sys.argv[1], sys.argv[2], sys.argv[3])
engine = sqlalchemy.create_engine(data)
engine.connect()
Base = declarative_base()


class State(Base):
    """State subclass inherting from Base class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
