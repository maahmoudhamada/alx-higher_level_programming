#!/usr/bin/python3
"""Script to list all rows in a table `State`"""


import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import asc


if __name__ == '__main__':
    connect_info = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.\
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = sqlalchemy.create_engine(connect_info, pool_pre_ping=True)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()

    for name, id in \
            session.query(State.name, State.id).order_by(asc(State.id)).all():
        print("{}: {}".format(id, name))
