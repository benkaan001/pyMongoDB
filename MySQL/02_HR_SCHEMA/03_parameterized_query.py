from multiprocessing.spawn import prepare
import mysql.connector
from config import get_database

# The first time we pass a SQL query statement to the cursor's execute method, the complier creates
# the prepared method.

#when passing multiple tuple values into the same query, ie injecting multiple rows into a table,
# make sure to create a 'prepared statment object' this way the query gets executed directly with passed
# parameters without being recomplied. In other words, for subsequent invocations, the preparation phase
# is skipped if the SQL statement is the same.

def get_it_employees(query, tuple):
    connection=get_database()
    cursor=connection.cursor(prepared=True)
    try:
            cursor.execute(query,tuple)
            records = cursor.fetchall()
            for record in records:
              print("Employee Full Name:", record[0], "\nDept_ID:", record[1], "\nJob_ID:", record[2])
              connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")



parameterized_query ="""
            SELECT CONCAT(first_name, " ", last_name) 'employee full name', department_id, job_id
            FROM hr.employees
            WHERE department_id= %s AND job_id=%s
            """

data_tuple=(60, 'IT_PROG')

get_it_employees(parameterized_query, data_tuple)

'''
Employee Full Name: Alexander Hunold
Dept_ID: 60
Job_ID: IT_PROG
Employee Full Name: Bruce Ernst
Dept_ID: 60
Job_ID: IT_PROG
Employee Full Name: David Austin
Dept_ID: 60
Job_ID: IT_PROG
Employee Full Name: Valli Pataballa
Dept_ID: 60
Job_ID: IT_PROG
Employee Full Name: Diana Lorentz
Dept_ID: 60
Job_ID: IT_PROG


'''

# we can also use bind the parameters

def get_listed_employees(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        employee_names_list = ['Elizabeth', 'Harrison', 'Charles']
        for name in employee_names_list:
            cursor.execute(f'{query}="{name}"')
            records = cursor.fetchall()
            for record in records:
              print("Employee Full Name:", record[0], "\nsalary:", record[1])
              connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")



repeating_query ="""
            SELECT CONCAT(first_name, " ", last_name) 'employee full name',
            ROUND(salary)
            FROM hr.employees
            WHERE first_name
            """


# get_listed_employees(repeating_query)

'''
Employee Full Name: Elizabeth Bates
salary: 7300
Employee Full Name: Harrison Bloom
salary: 10000
Employee Full Name: Charles Johnson
salary: 6200

'''

def get_listed_employees2(query, tuple_list):
    connection=get_database()
    cursor=connection.cursor(prepared=True)
    try:
        for name in tuple_list:
            cursor.execute(query,name)
            records = cursor.fetchall()
            for record in records:
              print("Employee Full Name:", record[0], "\nsalary:", record[1])
              connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")



repeating_query2 ="""
            SELECT CONCAT(first_name, " ", last_name) 'employee full name',
            ROUND(salary)
            FROM hr.employees
            WHERE first_name = %s
            """

tuple_list = [('Elizabeth',), ('Harrison',), ('Charles',)]


get_listed_employees2(repeating_query2, tuple_list)

'''
Employee Full Name: Elizabeth Bates
salary: 7300
Employee Full Name: Harrison Bloom
salary: 10000
Employee Full Name: Charles Johnson
salary: 6200

'''