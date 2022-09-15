from mysql.connector import Error
from config import get_database


def remove_duplicate_records(multi_query):

    connection = get_database()

    try:
        with connection.cursor() as cursor:
            for result in cursor.execute(multi_query):
                if result.with_rows:
                    records = result.fetchall()
                    for row in records:
                        print(row)

            connection.commit()

    except Error as e:
        print(e)


multi_query = """



"""

remove_duplicate_records(multi_query)
