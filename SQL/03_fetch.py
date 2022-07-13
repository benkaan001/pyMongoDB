import mysql.connector
from config import get_database

def get_january_hires(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print(record[4])  # 1992-01-23
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

# write a SQL query to find those employees who joined in the month of January

january_hires_query ="""
                        SELECT *
                        FROM employees
                        WHERE hire_date LIKE ('_____%01%___')

                        """


get_january_hires(january_hires_query)

