import mysql.connector
from config import get_database

def get_senior_managers(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print("DEPT:",record[0], " \tNAME:",record[1], "\tSALARY:",record[2], "\tEXPERIENCE:", record[3])
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

# Write a query to display department name, employee name (first_name, last_name), salary, num of years of experience
#of the manager for all managers whose experience is more than 15 years
senior_manager_query ="""
            SELECT d.department_name , CONCAT(e.first_name," ", e.last_name) AS name, e.salary,
            ROUND( (DATEDIFF(CURDATE(), hire_date))/365 ,1) as experience
            FROM employees e
            LEFT JOIN departments d
            ON e.department_id = d.department_id
            WHERE e.employee_id = d.manager_id
            AND
            DATEDIFF(CURDATE(), hire_date)/365 > 15

            """


get_senior_managers(senior_manager_query)

"""
DEPT: Administration    NAME: Jennifer Whalen   SALARY: 4400.00         EXPERIENCE: 34.9
DEPT: Marketing         NAME: Michael Hartstein SALARY: 13000.00        EXPERIENCE: 26.4
DEPT: Purchasing        NAME: Den Raphaely      SALARY: 11000.00        EXPERIENCE: 27.6
DEPT: Human Resources   NAME: Susan Mavris      SALARY: 6500.00         EXPERIENCE: 28.1
DEPT: Shipping          NAME: Adam Fripp        SALARY: 8200.00         EXPERIENCE: 25.3
DEPT: IT                NAME: Alexander Hunold  SALARY: 9000.00         EXPERIENCE: 32.6
DEPT: Public Relations  NAME: Hermann Baer      SALARY: 10000.00        EXPERIENCE: 28.1
DEPT: Sales             NAME: John Russell      SALARY: 14000.00        EXPERIENCE: 25.8
DEPT: Executive         NAME: Steven King       SALARY: 24000.00        EXPERIENCE: 35.1
DEPT: Finance           NAME: Nancy Greenberg   SALARY: 12000.00        EXPERIENCE: 27.9
DEPT: Accounting        NAME: Shelley Higgins   SALARY: 12000.00        EXPERIENCE: 28.1

"""