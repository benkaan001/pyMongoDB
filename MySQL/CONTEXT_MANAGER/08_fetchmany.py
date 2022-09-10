from mysql.connector import Error
from config import get_database

# It’s necessary to clean all unread results before executing
# any other statements on the same connection. Otherwise, an
# InternalError: Unread result found exception will be raised.


def get_top_five_movies(query):

    connection = get_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            for movie in cursor.fetchmany(size=5):
                print(movie)
            cursor.fetchall()
    except Error as e:
        print(e)


query = """
SELECT CONCAT(title, " (", release_year, ")"), collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
"""

get_top_five_movies(query)

"""
('Avengers: Endgame (2019)', 859)
('Titanic (1997)', 659)
('The Dark Knight (2008)', 535)
('Toy Story 4 (2019)', 435)
('The Lion King (1994)', 424)
"""

# replacing fetchmany() method with LIMIT on the query


def get_top_five_movies2(query):

    connection = get_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            for movie in cursor.fetchall():
                print(movie)
    except Error as e:
        print(e)


query2 = """
SELECT CONCAT(title, " (", release_year, ")"), collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
LIMIT 5
"""

get_top_five_movies2(query2)
