import sys
import MySQLdb

# import sqlalchemy
# import pymysql
# pymysql.install_as_MySQLdb()
# import pymysql as MySQLdb
# import MySQLdb import _mysql
# from MySQLdb.constants import FIELD_TYPE
# Define the database connection details
# username = sys.argv[1]
# password = sys.argv[2]
# database = sys.argv[3]
# my_conv = { FIELD_TYPE.LONG: int }
# db=_mysql.connect(conv=my_conv,host="localhost",user=username,password=password,database=database)
# r=db.store_result()
# # ...or...
# # r=db.use_result()
# r.fetch_row(maxrows=0)
# print(MySQLdb.__version__)
# print(sqlalchemy.__version__)


def dostg():
    # Open database connection
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    # db = MySQLdb.connect(host="localhost", user=u, password=p,
    # database=d, port=3306,collation = "utf8mb4_general_ci")
    db = MySQLdb.connect("localhost", u, p, d, 3306)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    # cursor.execute("ALTER TABLE states MODIFY COLUMN
    # name VARCHAR(250) COLLATE Latin1_General_CS_AS")

    cursor.execute("""SELECT *
FROM states WHERE name  = '{}'
ORDER BY id ASC; """.format(sys.argv[4]))
# COLLATE latin1_general_cs
#  "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format()
    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    for i in data:
        if i[1] == sys.argv[4]:
            print(i, sep="\n")

    # disconnect from server
    db.close()


if __name__ == "__main__":
    dostg()
