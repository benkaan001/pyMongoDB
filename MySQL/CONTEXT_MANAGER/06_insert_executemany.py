from mysql.connector import Error
from config import get_database


# executemany ( query_statement, iterable )

def insert_records(insert_reviewers_query, reviewers_records):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            cursor.executemany(insert_reviewers_query, reviewers_records)
            connection.commit()
            print("Transaction completed successfully!\nPrinting sample data:")
            cursor.execute(
                """SELECT * FROM reviewers WHERE first_name = "Amy" """)
            records = cursor.fetchall()
            print(records)
    except Error as e:
        print(e)


insert_reviewers_query = """
INSERT INTO reviewers
(first_name, last_name)
VALUES ( %s, %s )
"""

reviewers_records = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    ("John", "Wayne"),
    ("Thomas", "Stoneman"),
    ("Penny", "Hofstadter"),
    ("Mitchell", "Marsh"),
    ("Wyatt", "Skaggs"),
    ("Andre", "Veiga"),
    ("Sheldon", "Cooper"),
    ("Kimbra", "Masters"),
    ("Kat", "Dennings"),
    ("Bruce", "Wayne"),
    ("Domingo", "Cortes"),
    ("Rajesh", "Koothrappali"),
    ("Ben", "Glocker"),
    ("Mahinder", "Dhoni"),
    ("Akbar", "Khan"),
    ("Howard", "Wolowitz"),
    ("Pinkie", "Petit"),
    ("Gurkaran", "Singh"),
    ("Amy", "Farah Fowler"),
    ("Marlon", "Crafford"),
]

#insert_records(insert_reviewers_query, reviewers_records)

"""
Transaction completed successfully!
Printing sample data:
[(21, 'Amy', 'Farah Fowler')]
"""


def insert_records(insert_ratings_query, ratings_records):
    connection = get_database()
    try:
        with connection.cursor() as cursor:
            cursor.executemany(insert_ratings_query, ratings_records)
            connection.commit()
            print(
                "Transaction completed successfully!\nPrinting rating records 9 and above:")
            cursor.execute(
                """SELECT * FROM ratings """)
            records = cursor.fetchall()
            above_9_rated_movies = [row for row in records if row[0] >= 9]
            print(above_9_rated_movies)
    except Error as e:
        print(e)


insert_ratings_query = """
INSERT INTO ratings
(rating, movie_id, reviewer_id)
VALUES ( %s, %s, %s)
"""
ratings_records = [
    (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
    (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
    (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
    (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
    (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
    (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
    (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
    (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
    (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
    (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
    (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
    (9.8, 13, 1)
]

#insert_records(insert_ratings_query, ratings_records)


"""
Transaction completed successfully!
Printing rating records 9 and above:
[(6, 4, Decimal('9.7')),
(6, 10, Decimal('9.9')),
(13, 1, Decimal('9.8')),
(13, 3, Decimal('9.7')),
(14, 9, Decimal('9.9')),
(15, 13, Decimal('9.9')),
(23, 3, Decimal('9.8')),
(25, 6, Decimal('9.0')),
(30, 20, Decimal('9.5'))]

"""
