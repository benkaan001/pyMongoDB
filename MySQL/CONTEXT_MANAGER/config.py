from mysql.connector import connect
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
password = os.getenv("MYSQL_PWD")


def get_database():
    with connect(host='localhost', user='root', password=password, database='movie_rating') as connection:
        return connection


if __name__ == "__main__":
    connection = get_database()
