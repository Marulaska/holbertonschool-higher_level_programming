#!/usr/bin/python3
"""
Script to display values in the states table
of hbtn_0e_0_usa where name matches the given argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(
            host="localhost", port=3306, user=mysql_user,
            passwd=mysql_password, db=db_name, charset="utf8"
        )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

    cur = conn.cursor()

    try:
        query = "SELECT cities.id, cities.name, states.name"
        query += " FROM cities JOIN states"
        query += " ON cities.state_id = states.id"
        query += " WHERE states.name = %s"
        query += " ORDER BY cities.id ASC"
        cur.execute(query, (state_name,))
        results = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"Error executing SQL query: {e}")
        cur.close()
        conn.close()
        sys.exit(1)

    for row in results:
        print(row)

    cur.close()
    conn.close()
