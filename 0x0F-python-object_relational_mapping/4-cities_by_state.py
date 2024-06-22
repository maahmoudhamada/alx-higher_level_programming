#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys
import re

if __name__ == '__main__':
    av = sys.argv
    sql_user, sql_pass, db_name = av[1], av[2], av[3]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sql_user,
        passwd=sql_pass,
        db=db_name)
    cur = db.cursor()
    query = """
        SELECT states.id, cities.name, states.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
