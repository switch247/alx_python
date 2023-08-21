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
    db = MySQLdb.connect(host="localhost", user=u, password=p, database=d, port=3306,collation = "utf8mb4_general_ci")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    for i in data:
        if(i[1][0]!='n'):
            print(i, sep="\n")

    # disconnect from server
    db.close()


if __name__ == "__main__":
    dostg()
