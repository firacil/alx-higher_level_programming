#!/usr/bin/python3
"""module to connect to mysqdatabse"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    connect to aMYSQL db and prints all states sorted by id
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
