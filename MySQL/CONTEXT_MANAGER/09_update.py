from mysql.connector import Error
from config import get_database


def update_reviewer_name(update_query, confirmation_query):

    connection = get_database()

    try:
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            connection.commit()
    except Error as e:
        print(e)
    else:
        with connection.cursor() as cursor:
            cursor.execute(confirmation_query)
            result = cursor.fetchall()
            for row in result:
                id, first_name, last_name = row
                print(f"\tid:{id} Name:{first_name} {last_name}\n")


update = """
UPDATE
    reviewers
SET
    last_name = "Cooper"
WHERE
    first_name = "Amy"

"""


confirm = """
SELECT * FROM reviewers WHERE first_name = "Amy" """


update_reviewer_name(update, confirm)

""""
    id:21 Name:Amy Cooper

    id:43 Name:Amy Cooper
"""
