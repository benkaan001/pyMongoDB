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


multi_query = """
SELECT c1.id
FROM cars c1
INNER JOIN cars c2
ON c1.brand = c2.brand AND c1.model = c2.model
WHERE c1.id > c2.id ;

SELECT *
FROM cars
WHERE id IN
            (SELECT c1.id
            FROM cars c1
            INNER JOIN cars c2
            ON c1.model = c2.model AND c1.brand = c2.brand
            WHERE c1.id > c2.id);
"""

get_duplicate_records(multi_query)
