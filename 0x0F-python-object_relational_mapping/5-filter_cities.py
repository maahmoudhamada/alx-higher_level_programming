#!/usr/bin/python3
"""Script takes in the name of a state as an arg and lists all cities"""


import MySQLdb
import sys

if __name__ == "__main__":
    av = sys.argv
    sql_user, sql_pass, db_name, stat_name = av[1], av[2], av[3], av[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sql_user,
        passwd=sql_pass,
        db=db_name
    )

    cur = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id
    """
    cur.execute(query, (stat_name,))
    out = [row[0] for row in cur.fetchall()]
    for i in range(len(out)):
        print("{}".format(out[i]), end="")
        if i != len(out) - 1:
            print(", ", end="")
    print("")
