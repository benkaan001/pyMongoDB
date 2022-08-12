import mysql.connector
from config import get_database

def get_new_salaries(query):
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

# GIVE THE CORRESPONDING RAISES TO ALL EMPLOYEES ACCORDINGLY
# PRINT employee_id, first_name, job_id, salary, *new_salary
# ROUND UP the salaries by 2 decimal points
"""
    IF job_id has '_PROG'       - 30%
                  '_CLERK'      - 25%
                  '_MAN'        - 20%
                  '_REP'        - 20%
                  ALL ELSE      - 40%

"""
raise_query ="""
            SELECT employee_id, first_name, job_id, salary,
            CASE job_id
                WHEN 'IT_PROG' THEN ROUND(salary * 1.5, 2)
                WHEN 'PU_CLERK%' OR 'ST_CLERK' OR 'SH_CLERK' THEN ROUND(salary * 1.25, 2)
                WHEN  'SA_REP' OR 'MK_REP' OR 'HR_REP' THEN ROUND(salary * 1.2,2)
                ELSE ROUND(salary * 1.4,2)
            END new_salary
            FROM employees
            """


get_new_salaries(raise_query)
