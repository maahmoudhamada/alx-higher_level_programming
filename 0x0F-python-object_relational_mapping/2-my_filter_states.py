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
    cur.execute("""SELECT * FROM states
        WHERE name='{}'
        ORDER BY states.id ASC""".format(name_search))
    print(cur.fetchone())
    cur.close()
    db.close()
