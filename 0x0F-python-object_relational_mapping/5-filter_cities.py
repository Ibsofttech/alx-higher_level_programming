#!/usr/bin/python3
""" A python module that prints all cities from a given state """
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_arg = sys.argv[4]
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cusr = db.cursor()
    cusr.execute("SELECT c.name FROM cities as c\
                     INNER JOIN states as s\
                        ON c.state_id = s.id\
                           WHERE s.name = %s", (state_arg,))
    cities = cusr.fetchall()

    print(", ".join([city[0] for city in cities]))

    cusr.close()
    db.close()
