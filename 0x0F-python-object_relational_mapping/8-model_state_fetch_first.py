#!/usr/bin/python3
"""Script to print first record in a table"""
import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    connect_info = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = sqlalchemy.create_engine(connect_info, pool_pre_ping=True)
    engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    if state is None:
        pass
    else:
        print("{}: {}".format(state.id, state.name))
