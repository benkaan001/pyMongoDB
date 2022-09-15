from mysql.connector import connect
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
password = os.getenv("MYSQL_PWD")


def get_database():

    connection = connect(
        user="root", host="localhost", password=password, database="cars_db2"
    )

    return connection


if __name__ == "__main__":
    connection = get_database()
