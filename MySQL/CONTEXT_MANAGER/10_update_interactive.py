from getpass import getpass
from mysql.connector import connect, Error

# To pass multiple queries to a single cursor.execute(), set multi to True
# When multi=True, cursor.execute() will return an iterator that we need to unpack
# To avoid the error in case no result set is fetched after the query is run,
# check if the result has produced any rows by using the with_rows property, then call fetchall()


def update_reviewer_rating(multi_update_query):

    try:
        with connect(
            host="localhost",
            user=input("Enter username: "),
            password=input("Enter password: "),
            database="movie_rating",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(multi_update_query, multi=True):
                    if result.with_rows:
                        print(result.fetchall())
                connection.commit()

    except Error as e:
        print(e)


movie_id = input("Enter movie id: ")
reviewer_id = input("Enter reviewer id: ")
new_rating = input("Enter new rating: ")


update_query = f"""
UPDATE
    ratings
SET
    rating = {new_rating}
WHERE
    movie_id = {movie_id} AND reviewer_id={reviewer_id};

SELECT *
FROM ratings
WHERE
    movie_id ={movie_id} AND reviewer_id={reviewer_id}

"""

update_reviewer_rating(update_query)

"""
Enter movie id: 18
Enter reviewer id: 15
Enter new rating: 5.0
Enter username: root
Enter password: ************
[(18, 15, Decimal('5.0'))]
"""
