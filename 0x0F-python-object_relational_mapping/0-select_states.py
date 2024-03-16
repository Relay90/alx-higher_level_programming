#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL Server:", e)
        sys.exit(1)

    # Execute query to fetch states
    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error executing query:", e)
        cursor.close()
        db.close()
        sys.exit(1)

    # Display results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
