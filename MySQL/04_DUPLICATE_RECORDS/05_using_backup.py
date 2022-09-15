from mysql.connector import Error
from config import get_database


def create_backup_table(multi_query):

    try:
        connection = get_database()
        with connection.cursor() as cursor:
            for result in cursor.execute(multi_query, multi=True):
                if result.with_rows:
                    records = cursor.fetchall()
                    for row in records:
                        print(row)

            connection.commit()

    except Error as e:
        print(e)


multi_query = """
DROP TABLE IF EXISTS cars_backup;

CREATE TABLE IF NOT EXISTS cars_backup
AS
SELECT * FROM cars
WHERE 1=0;

INSERT INTO cars_backup
SELECT * FROM cars
WHERE id IN
            (SELECT MAX(id)
            FROM cars
            GROUP BY brand, model
            HAVING COUNT(*) > 1);

SELECT * FROM cars_backup;

DROP TABLE cars_backup;

"""

create_backup_table(multi_query)
