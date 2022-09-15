from config import get_database
from mysql.connector import Error

# Requirement: Delete duplicate data from cars table.
# Duplicate record is identified based on the model and brand name.


def select_duplicate_records(multi_query):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            for result in cursor.execute(multi_query, multi=True):
                if result.with_rows:
                    records = result.fetchall()
                    for record in records:
                        print(record)
            connection.commit()
    except Error as e:
        print(e)


multi_query = """
SELECT MAX(id)
FROM cars
GROUP BY model, brand
HAVING COUNT(*) > 1;


SELECT * FROM cars
WHERE id IN
            (SELECT MAX(id)
            FROM cars
            GROUP BY model, brand
            HAVING COUNT(id) > 1)

"""
select_duplicate_records(multi_query)
