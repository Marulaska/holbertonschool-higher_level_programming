#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def list_states(mysql_user, mysql_password, db_name):
    """
    Connects to the MySQL database
    and lists all states in ascending order by states.id.

    Args:
        mysql_user (str): MySQL username.
        mysql_password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
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
        cur.execute("SELECT * FROM states ORDER BY id ASC")
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


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./list_states.py" +
              "<mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
