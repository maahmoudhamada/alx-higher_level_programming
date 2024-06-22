#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys

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
    cur.execute("""SELECT * FROM states
        ORDER BY states.id""")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
