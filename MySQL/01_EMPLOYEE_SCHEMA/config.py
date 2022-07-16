import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv


def get_database():

    load_dotenv(find_dotenv())
    password=os.getenv("MYSQL_PWD")

    connection = mysql.connector.connect(host="localhost", user="root", password=password, database='employee_db')

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    # cursor = connection.cursor()


    # Create the database for our example (we will use the same database throughout the tutorial
    return connection

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    connection= get_database()