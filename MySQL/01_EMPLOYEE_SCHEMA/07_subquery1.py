
import mysql.connector
from config import get_database

def find_employees_with_higher_salaries(query):
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

#Write a query to find the name emp_name and the salary of the employees
# who have a higher salary than the employee whose emp_name='TUCKER'

salary_query ="""
                SELECT emp_name, salary
                FROM employees
                WHERE salary > (SELECT salary
                                FROM employees
                                WHERE emp_name = 'TUCKER')
                ORDER BY salary;
            """


find_employees_with_higher_salaries(salary_query)

'''
('ADELYN', 1700.0)
('CLARE', 2550.0)
('BLAZE', 2750.0)
('JONAS', 2957.0)
('SCARLET', 3100.0)
('FRANK', 3100.0)
('KAYLING', 6000.0)

'''