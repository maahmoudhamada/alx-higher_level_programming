#!/usr/bin/python3
"""Script to print all record with letter a within it in a table"""
import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    stateName = sys.argv[4]
    connect_info = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = sqlalchemy.create_engine(connect_info, pool_pre_ping=True)
    engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()
    records = session.query(State).all()

    stateID = None
    for record in records:
        if record.name == stateName:
            stateID = record.id
    if stateID is None:
        print("Not found")
    else:
        print(stateID)
