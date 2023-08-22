import MySQLdb
import sys


def search_states(username, password, database):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Prepare the SQL query with a parameterized query
        query = """SELECT cities.id, cities.name, states.name FROM cities  INNER JOIN states ON
        cities.state_id = states.id ORDER BY id ASC; """

        # Execute the query with the state name as a parameter
        cursor.execute(query)

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Display the results
        if rows:
            for row in rows:
                print(row)
        else:
            # print("No matching states found.")
            pass

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # state_name = sys.argv[4]

    # Call the search_states function with the provided arguments
    search_states(username, password, database)
