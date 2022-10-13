from mysql.connector import Error
from config import get_database

# for mysql the syntax is CREATE OR REPLACE VIEW

view_name = "high_paid_employees_view"
filter_clause = "WHERE salary >= 10000"

high_paid_employees_view_query = f"""
CREATE OR REPLACE VIEW {view_name}
AS
SELECT *
FROM employees
{filter_clause}
"""


def create_view(query):

    connection = get_database()

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            print(f"{view_name} was successful!")
    except Error as e:
        print(e)


create_view(high_paid_employees_view_query)  # high_paid_employees_view was successful!
