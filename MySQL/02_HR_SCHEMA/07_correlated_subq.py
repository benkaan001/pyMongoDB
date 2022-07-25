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

# Write a query to find the name (first_name, last_name), and salary of
# the employees whose salary is equal to the minimum salary for their job grade.

min_salary_query="""
                    SELECT CONCAT (first_name, " ", last_name) name,salary
                    FROM employees e
                    WHERE e.salary =
                    (SELECT min_salary
                    FROM jobs j
                    WHERE e.job_id = j.job_id)
                    """
# insert_subquery(min_salary_query)

#Write a query to find the name (first_name, last_name), and salary of the employees
# who earns more than the average salary and works in any of the IT departments

avg_IT_salary_query= """
                    SELECT CONCAT (first_name, " ", last_name) name,salary
                    FROM employees
                    WHERE salary > (SELECT AVG(salary) from employees)
                    AND department_id =
                    (SELECT department_id
                    FROM departments
                    WHERE department_name = 'IT')
                    """

# insert_subquery(avg_IT_salary_query)

#Write a query to find the name (first_name, last_name) of the employees who are not supervisors.

supervisor_query = """
                    SELECT CONCAT(e.first_name, " ",e.last_name) name
                    FROM employees e
                    WHERE NOT EXISTS
                        (SELECT 1
                        FROM employees m
                        WHERE e.employee_id = m.manager_id)
                    """

# insert_subquery(supervisor_query)

#Write a query to display the employee ID, first name, last name, and department names of all employees

select_department_query="""
                        SELECT CONCAT (first_name, " ", last_name) name,salary,
                                (SELECT department_name
                                 FROM departments d
                                WHERE d.department_id = e.department_id) as department_name
                        FROM employees e

                        """

# insert_subquery(select_department_query)


#Write a query to display the employee ID, first name, last name, salary of all employees
# whose salary is above average for their departments.

avg_dept_salary_query= """
                        SELECT CONCAT (first_name, " ", last_name) name,salary
                        FROM employees e
                        WHERE salary >
                        (SELECT AVG(salary)
                        FROM employees s
                        WHERE s.department_id = e.department_id)
                        """

# insert_subquery(avg_dept_salary_query)