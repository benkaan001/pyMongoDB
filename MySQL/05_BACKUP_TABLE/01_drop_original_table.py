from config import get_database
from mysql.connector import Error


def create_backup_table(multiquery):

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


multiquery = """
DROP TABLE IF EXISTS cars_backup;

CREATE TABLE IF NOT EXISTS cars_backup
AS
SELECT * FROM cars
WHERE 1=0;

INSERT INTO cars_backup
AS
SELECT *
FROM cars
WHERE id NOT IN
                (SELECT MAX(id)
                FROM cars
                GROUP BY brand, model
                HAVING COUNT(*) > 1);

DROP TABLE cars;

ALTER TABLE cars_backup RENAME TO cars;
"""

create_backup_table(multiquery)
