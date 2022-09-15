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
SELECT *, row_number() OVER(PARTITION BY model,brand) row_num
FROM cars;

SELECT id
FROM (SELECT *, row_number() OVER(PARTITION BY model,brand) row_num
FROM cars) x
WHERE x.row_num > 1;

SELECT *
FROM cars
WHERE id IN
			(SELECT id
			FROM (SELECT *, row_number() OVER(PARTITION BY model,brand) row_num FROM cars) x
			WHERE x.row_num > 1);

"""
get_duplicate_records(multi_query)
