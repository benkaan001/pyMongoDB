from mysql.connector import connect
from dotenv import load_dotenv, find_dotenv
import os


def get_database():

    load_dotenv(find_dotenv())
    password = os.getenv("MYSQL_PWD")
    connection = connect(
        host="localhost", user="root", password=password, database="cars_db"
    )

    return connection


if __name__ == "__main__":
    connection = get_database()
