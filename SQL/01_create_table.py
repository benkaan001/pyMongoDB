import mysql.connector
from config import get_database


def create_table(table_query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(table_query)
        connection.commit()
        print(".......Table Inserted!")
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")



department_table= """CREATE TABLE department (
                 dep_id INT PRIMARY KEY,
                 dep_name VARCHAR(20),
                 dep_location VARCHAR(15)
                 )"""

employees_table= """CREATE TABLE employees (
                 emp_id INT PRIMARY KEY,
                 emp_name VARCHAR(20),
                 job_name VARCHAR(10),
                 manager_id INT,
                 hire_date DATE,
                 salary DOUBLE(10,2),
                 commission DOUBLE(7,2),
                 dept_id INTEGER REFERENCES department_table(dept_id)
                 )"""

salary_grade_table="""CREATE TABLE salary_grade (
                 grade INT PRIMARY KEY,
                 min_salary INT,
                 max_salary INT
                 )"""

# create_table(department_table)

# create_table(employees_table)

create_table(salary_grade_table)



