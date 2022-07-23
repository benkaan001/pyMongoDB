import mysql.connector
from config import get_database

def insert_subquery(query):
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

# Write a query to find the name (first_name, last_name) and the salary of the employees
# who have a higher salary than the employee whose last_name='Bull'.
salary_comparison_query ="""
            SELECT CONCAT(first_name," ", last_name) name, ROUND(salary,1)
            FROM employees
            WHERE salary >
                        (SELECT salary
                        FROM employees
                        WHERE last_name = 'Bull')
            ORDER BY name
            """


# insert_subquery(salary_comparison_query)

#Write a query to find the name (first_name, last_name)
# of the employees who have a manager who is based in a US-based department.

dept_comparison_query ="""
            SELECT CONCAT (first_name, " ", last_name)
            FROM employees
            WHERE manager_id IN
                            (SELECT employee_id
                            FROM employees
                            WHERE department_id IN
                                        (SELECT department_id
                                        FROM departments
                                        WHERE location_id IN
                                                (SELECT location_id
                                                FROM locations
                                                WHERE country_id = 'US')))

            """

# insert_subquery(dept_comparison_query)

manager_query ="""
                SELECT CONCAT (first_name, " ", last_name)
                FROM employees
                WHERE employee_id IN
                                (SELECT manager_id
                                 FROM employees )
                """

# insert_subquery(manager_query)

