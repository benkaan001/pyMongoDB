#  (14) Write a query to get the average salary for all departments employing more than 10 employees.
import mysql.connector
from config import get_database


def get_average_salary(query):
    try:
        connection = get_database()
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print("Printing average salary for department employing more than 10 employees\n")
        for row in records:
            print(f"Department Name: {row[0]}")
            print(f"Average Salary: {row[1]}")
            print(f"Employee Count: {row[2]}\n")
    except (Exception, mysql.connector.Errror) as error:
        print("Ups! We have an error: ", error)
    finally:
        cursor.close()
        connection.close()
        print("Connection closed successfully.")


avg_salary_query = """
                    SELECT d.department_name, AVG(e.salary) avg_salary, COUNT(e.employee_id) employee_count
                    FROM departments d
                    INNER JOIN employees e
                    ON e.department_id = d.department_id
                    GROUP BY d.department_name HAVING COUNT(e.employee_id) > 10
"""

get_average_salary(avg_salary_query)

"""
Printing average salary for department employing more than 10 employees

Department name: Shipping
Average Salary: 3475.555556
Employee Count: 45

Department name: Sales
Average Salary: 8955.882353
Employee Count: 34

"""
