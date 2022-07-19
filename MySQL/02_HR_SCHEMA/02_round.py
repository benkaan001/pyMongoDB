import mysql.connector
from config import get_database

def find_employees_earning_above_average(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print("Employee Full Name:", record[0], "\nsalary:", record[1], "\naverage:", record[4], "\nratio:", record[5])
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")


# average without round 6600.000
# ROUND(variable, # of decimal places to keep) => ROUND(1.111111, 2) = 1.11

average_salary_query ="""
            SELECT CONCAT(e.first_name, " ", e.last_name) 'employee full name',
            ROUND(e.salary), j.min_salary minimum, j.max_salary maximum,
            ROUND((j.min_salary + j.max_salary)/2) average,
            ROUND(e.salary/ROUND((j.min_salary+j.max_salary)/2),2) ratio
            FROM employees e
            LEFT JOIN jobs j
            ON e.job_id = j.job_id
            WHERE e.salary >((j.min_salary + j.max_salary)/2)
            ORDER BY salary/average DESC

            """


find_employees_earning_above_average(average_salary_query)

'''
Employee Full Name: Daniel Faviet
salary: 9000
average: 6600
ratio: 1.36
Employee Full Name: Hermann Baer
salary: 10000
average: 7500
ratio: 1.33
Employee Full Name: Alexander Hunold
salary: 9000
average: 7000
ratio: 1.29
.
.
.
Employee Full Name: Alexis Bull
salary: 4100
average: 4000
ratio: 1.03
'''