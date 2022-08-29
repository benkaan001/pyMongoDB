from config import get_database
from mysql.connector import Error


def fetch_records(select_movies_query):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            records = cursor.fetchall()
            for row in records:
                print(row)
    except Error as e:
        print(e)


top_5_records_query = "SELECT * FROM movies LIMIT 5"
fetch_records(top_5_records_query)
"""
(1, 'Forrest Gump', 1994, 'Drama', 330)
(2, '3 Idiots', 2009, 'Drama', 2)
(3, 'Eternal Sunshine of the Spotless Mind', 2004, 'Drama', 35)
(4, 'Good Will Hunting', 1997, 'Drama', 138)
(5, 'Skyfall', 2012, 'Action', 305)

"""

# return rows 3 to 7
specific_range_query = " SELECT * FROM movies LIMIT 2,5"
fetch_records(specific_range_query)
"""
(3, 'Eternal Sunshine of the Spotless Mind', 2004, 'Drama', 35)
(4, 'Good Will Hunting', 1997, 'Drama', 138)
(5, 'Skyfall', 2012, 'Action', 305)
(6, 'Gladiator', 2000, 'Action', 189)
(7, 'Black', 2005, 'Drama', 3)
"""
