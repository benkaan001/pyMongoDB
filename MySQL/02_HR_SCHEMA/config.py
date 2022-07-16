import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv


def get_database():

    load_dotenv(find_dotenv())
    password=os.getenv("MYSQL_PWD")

    connection = mysql.connector.connect(host="localhost", user="root", password=password, database='hr')


    return connection

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    connection= get_database()