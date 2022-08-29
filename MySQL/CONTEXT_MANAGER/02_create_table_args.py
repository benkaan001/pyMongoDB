from mysql.connector import Error
from config import get_database

"""
Reusing the same cursor for multiple executions.
All executions become one ATOMIC transaction rather than multiple separate transactions.

***** A multi rollback() actions would be treated as one ATOMIC transaction as well.
"""


def create_table(*args):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            for arg in args:
                cursor.execute(arg)
            connection.commit()
            print("Table crated!")
    except Error as e:
        print(e)


movies_table_query = """
CREATE TABLE IF NOT EXISTS movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(10),
    collection_in_mil INT
)
"""

reviewers_table_query = """
CREATE TABLE IF NOT EXISTS reviewers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""

ratings_table_query = """
CREATE TABLE IF NOT EXISTS ratings(
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""

create_table(movies_table_query, reviewers_table_query, ratings_table_query)
