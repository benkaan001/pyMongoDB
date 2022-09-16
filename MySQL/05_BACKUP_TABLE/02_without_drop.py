from config import get_database
from mysql.connector import Error


def truncate_original_table(multiquery):

    connection = get_database()
    try:
        with connection.cursor() as cursor:
            for result in cursor.execute(multiquery, multi=True):
                if result.with_rows:
                    records = result.fetchall()
                    for row in records:
                        print(row)

        connection.commit()

    except Error as e:
        print(e)


multi_query = """
DROP TABLE IF EXISTS cars_backup;

CREATE TABLE IF NOT EXISTS cars_backup
AS
SELECT *
FROM cars
WHERE 1=0;

INSERT INTO cars_backup
AS
SELECT *
FROM cars
WHERE id NOT IN
                (SELECT MIN(id)
                FROM cars
                GROUP BY model, brand
                HAVING COUNT(id) > 1 )

TRUNCATE table cars;

INSERT INTO cars
AS
SELECT * FROM cars_backup;

DROP TABLE cars_backup;

"""

truncate_original_table(multi_query)
