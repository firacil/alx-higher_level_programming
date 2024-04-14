#!/usr/bin/python3
"""
    script to lists all states with
    a name starting from arguments
    from the database hbtn_0e_0_usa
    and safer from sql injection
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connect to mysql and prints all states starts by upper N
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                   %(name)s ORDER BY id ASC", {'name': argv[4]})
    rows = cursor.fetchall()
    for row in rows:
        print(row)
