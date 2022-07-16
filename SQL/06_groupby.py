
import mysql.connector
from config import get_database

def find_max_senior_salary(query):
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

# write a SQL query to find the max salary for each senior whose experience is more than 27 years

max_salary_query ="""
                        SELECT MAX(salary), dept_id
                        FROM employees
                        WHERE TIMESTAMPDIFF( YEAR, hire_date, CURDATE() ) > 27
                        GROUP BY dept_id;
                        """


find_max_senior_salary(max_salary_query)

'''
(6000.0, 1001)
(3100.0, 2001)
(2750.0, 3001)

'''