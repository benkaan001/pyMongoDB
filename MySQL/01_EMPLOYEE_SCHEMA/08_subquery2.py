import mysql.connector
from config import get_database

def get_marketing_emps(query):
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

#Write a query to find the name of all employees who works in MARKETING

marketing_employees_query ="""
                            SELECT emp_name 'MARKETING TEAM'
                            FROM employees
                            WHERE dept_id  = (
                                            SELECT dept_id
                                            FROM department
                                            WHERE dept_name = 'MARKETING');
                        """


get_marketing_emps(marketing_employees_query)