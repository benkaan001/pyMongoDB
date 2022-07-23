import mysql.connector
from config import get_database

def find_senior_emps(query):
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

# write a SQL query to find those employees whose experience is more than 27 years in ascending order.

senior_emps_query ="""
                        SELECT *
                        FROM employees
                        WHERE TIMESTAMPDIFF( YEAR, hire_date, CURDATE() ) > 27
                        ORDER BY hire_date ASC;
                        """


find_senior_emps(senior_emps_query)
'''
(63679, 'SANDRINE', 'CLERK', 69062, datetime.date(1990, 12, 18), 900.0, None, 2001)
(64989, 'ADELYN', 'SALESMAN', 66928, datetime.date(1991, 2, 20), 1700.0, 400.0, 3001)
(65271, 'WADE', 'SALESMAN', 66928, datetime.date(1991, 2, 22), 1350.0, 600.0, 3001)
(65646, 'JONAS', 'MANAGER', 68319, datetime.date(1991, 4, 2), 2957.0, None, 2001)
(66928, 'BLAZE', 'MANAGER', 68319, datetime.date(1991, 5, 1), 2750.0, None, 3001)
(67832, 'CLARE', 'MANAGER', 68319, datetime.date(1991, 6, 9), 2550.0, None, 1001)
(68454, 'TUCKER', 'SALESMAN', 66928, datetime.date(1991, 9, 8), 1600.0, 0.0, 3001)
(66564, 'MADDEN', 'SALESMAN', 66928, datetime.date(1991, 9, 28), 1350.0, 1500.0, 3001)
(68319, 'KAYLING', 'PRESIDENT', None, datetime.date(1991, 11, 18), 6000.0, None, 1001)
(69000, 'JULIUS', 'CLERK', 66928, datetime.date(1991, 12, 3), 1050.0, None, 3001)
(69062, 'FRANK', 'ANALYST', 65646, datetime.date(1991, 12, 3), 3100.0, None, 2001)
(69324, 'MARKER', 'CLERK', 67832, datetime.date(1992, 1, 23), 1400.0, None, 1001)
'''