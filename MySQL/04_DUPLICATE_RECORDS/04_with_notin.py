from mysql.connector import Error
from config import get_database


def get_duplicate_records(multi_query):

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


# changing up MAX TO MIN
mutli_query = """
SELECT MIN(id)
FROM cars
GROUP BY model, brand
HAVING COUNT(*) > 1;

SELECT *
FROM cars
WHERE ID NOT IN
                (SELECT MIN(id)
                FROM cars
                GROUP BY model, brand
                HAVING COUNT(*) > 1);
"""
get_duplicate_records(mutli_query)
