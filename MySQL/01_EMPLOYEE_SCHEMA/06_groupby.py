
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
# list by department name in alphabetical order

max_salary_query ="""
                        SELECT MAX(salary), d.dept_name
                        FROM employees e
                        LEFT JOIN department d
                        ON e.dept_id = d.dept_id
                        WHERE TIMESTAMPDIFF( YEAR, hire_date, CURDATE() ) > 27
                        GROUP BY dept_name
                        ORDER BY dept_name ASC;
                        """


find_max_senior_salary(max_salary_query)

'''
(3100.0, 'AUDIT')
(6000.0, 'FINANCE')
(2750.0, 'MARKETING')

'''