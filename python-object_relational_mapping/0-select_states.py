import sys
# import sqlalchemy
# import pymysql
# pymysql.install_as_MySQLdb()
# import pymysql as MySQLdb

import MySQLdb
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
    db = MySQLdb.connect("localhost",sys.argv[1],sys.argv[2],sys.argv[3],3306 )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT * FROM states")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    print (data)

    # disconnect from server
    db.close()

if __name__ == "__main__":
    dostg()

