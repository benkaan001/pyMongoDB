import mysql.connector
from config import get_database
"""

SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
"""
def get_promoted_employees(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record)
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

# find employees who have received promotion in the last 10 years
# display first_name, job_id, start_date, end_date, years_of_service

promotion_query = """
                SELECT e.first_name, j.job_id, YEAR(j.start_date) "START_DATE", YEAR(j.end_date) "END_DATE",
                ABS(YEAR(j.start_date) - YEAR(j.end_date)) "YEARS_OF_SERVICE"
                FROM employees e
                INNER JOIN job_history j
                ON e.employee_id = j.employee_id
                WHERE TIMESTAMPDIFF(YEAR,j.start_date, j.end_date) < 10
                GROUP BY e.first_name, j.job_id
                """

get_promoted_employees(promotion_query)