import mysql.connector
from config import get_database

def get_total_raise(query):
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

# calculate the total raise

raise_query ="""
            SELECT employee_id, first_name, job_id, salary,
            CASE job_id
                WHEN 'IT_PROG' THEN salary * 1.5 - salary
                WHEN 'PU_CLERK%' OR 'ST_CLERK' OR 'SH_CLERK' THEN salary * 1.25 - salary
                WHEN  'SA_REP' OR 'MK_REP' OR 'HR_REP' THEN salary * 1.2 - salary
                ELSE salary * 1.4 - salary
            END total_raise
FROM employees

            """


get_total_raise(raise_query)