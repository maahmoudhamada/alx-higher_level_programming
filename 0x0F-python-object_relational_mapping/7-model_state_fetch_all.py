#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc


av = sys.argv
info = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(av[1], av[2], av[3])
engine = sqlalchemy.create_engine(info)
engine.connect()

Session = sessionmaker(engine)
session = Session()
rows = session.query(State).order_by(asc(State.id)).all()

for row in rows:
    print("{}: {}".format(row.id, row.name))
