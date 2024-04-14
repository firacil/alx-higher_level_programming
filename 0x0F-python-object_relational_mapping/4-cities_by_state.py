#!/usr/bin/python3
"""
script that lists all cities from database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    script will list all cities in states
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states ON cities.state_id \
                   = states.id ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
