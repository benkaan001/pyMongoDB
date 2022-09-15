from mysql.connector import Error, connect
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
password = os.getenv("MYSQL_PWD")


def create_inject_database(multi_query):
    try:
        with connect(
            user="root", host="localhost", password=password, database="cars_db2"
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(multi_query, multi=True):
                    if result.with_rows:
                        records = result.fetchall()
                        for row in records:
                            print(row)
    except Error as e:
        print(e)


multi_query = """
CREATE DATABASE IF NOT EXISTS cars_db2;

CREATE TABLE IF NOT EXISTS cars
(
    id INT,
    model VARCHAR(50),
    brand VARCHAR(50),
    color VARCHAR(30),
    make INT
);

INSERT INTO cars VALUES (1, 'Model S', 'Tesla', 'Blue', 2018);
INSERT INTO cars VALUES (2, 'EQS', 'Mercedes-Benz', 'Black', 2022);
INSERT INTO cars VALUES (3, 'iX', 'BMW', 'Red', 2022);
INSERT INTO cars VALUES (4, 'Ioniq 5', 'Hyundai', 'White', 2021);
INSERT INTO cars VALUES (1, 'Model S', 'Tesla', 'Blue', 2018);
INSERT INTO cars VALUES (4, 'Ioniq 5', 'Hyundai', 'White', 2021);


SELECT * FROM cars;

"""

create_inject_database(multi_query)
