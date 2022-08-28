from config import get_database
from mysql.connector import Error


def create_table(table_query):
    try:
        connection = get_database()
        with connection.cursor() as cursor:
            cursor.execute(table_query)
            connection.commit()
            print("query created!")
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


queries = [movies_table_query, reviewers_table_query, ratings_table_query]
for query in queries:
    create_table(query)
