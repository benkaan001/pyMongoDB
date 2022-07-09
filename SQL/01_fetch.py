import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# second arg is optional default
password=os.getenv('MYSQL_PWD')


connection = mysql.connector.connect(host='localhost', user='root', password=password, database='Computers')
cursor = connection.cursor()
query= 'SELECT * FROM computers.computer'
cursor.execute(query)

# print(cursor.fetchone())
# print(cursor.fetchmany())
# print(cursor.fetchmany(3))
print(cursor.fetchall())

cursor.close()
connection.close()