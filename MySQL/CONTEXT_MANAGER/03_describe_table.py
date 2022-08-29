from config import get_database
from mysql.connector import Error


def describe_table(*args):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            for arg in args:
                cursor.execute(arg)
                records = cursor.fetchall()
                for row in records:
                    print(row)
    except Error as e:
        print(e)


desc_movies_query = "DESCRIBE movies"
desc_ratins_query = "DESCRIBE ratings"
desc_reviewers_query = "DESCRIBE reviewers"


describe_table(desc_movies_query)

"""
('id', b'int', 'NO', 'PRI', None, 'auto_increment')
('title', b'varchar(100)', 'YES', '', None, '')
('release_year', b'year', 'YES', '', None, '')
('genre', b'varchar(10)', 'YES', '', None, '')
('collection_in_mil', b'int', 'YES', '', None, '')
"""
