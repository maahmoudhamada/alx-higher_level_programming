#!/usr/bin/python3
"""script takes in an arg and displays values where name matches the args."""

import MySQLdb
import sys
import re

if __name__ == '__main__':
    av = sys.argv
    sql_user, sql_pass, db_name, name_search = av[1], av[2], av[3], av[4]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sql_user,
        passwd=sql_pass,
        db=db_name)
    cur = db.cursor()
    query = """
        SELECT * FROM states
        WHERE name
        LIKE BINARY '{}'
        ORDER BY states.id ASC"""
    cur.execute(query.format(name_search))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    cur.close()
    db.close()
