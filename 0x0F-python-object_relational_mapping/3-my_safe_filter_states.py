#!/usr/bin/python3
"""
This script is not safe from SQL injection.
"""


import sys
import MySQLdb
if __name__ == "__main__":
    states = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = states.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print("{}".format(row))
    cur.close()
    states.close()
