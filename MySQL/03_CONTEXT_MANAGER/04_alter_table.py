from config import get_database
from mysql.connector import Error


def alter_table(alter_table_query, show_table_query):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
            cursor.execute(show_table_query)
            # fetchall fetches rows from only the last executed query, which is show_table_query
            records = cursor.fetchall()
            print(records)
            for row in records:
                if row[0] == 'collection_in_mil':
                    print(row)
    except Error as e:
        print(e)


alter_table_query = """
ALTER TABLE movies
MODIFY COLUMN collection_in_mil DECIMAL(4,1)
"""

show_table_query = "DESCRIBE TABLE movies"


alter_table(alter_table_query, show_table_query)

"""
('collection_in_mil', b'decimal(4,1)', 'YES', '', None, '')
"""
