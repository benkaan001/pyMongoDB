from mysql.connector import connect, Error
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
password = os.getenv("MYSQL_PWD")


def create_db(query):
    try:
        with connect(host='localhost', user='root', password=password) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(" Success: DB crated!")
    except Error as e:
        print(e)


create_db_query = "CREATE DATABASE IF NOT EXISTS movie_rating"

create_db(create_db_query)
