import mysql.connector
from config import get_database

def insert_and_delete(query1,query2):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query1)
        records = cursor.fetchall()
        connection.commit()
        print(records)

        cursor2=connection.cursor()
        cursor2.execute(query2)
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")



first_query ="""
                SELECT * FROM employees
                WHERE first_name = "Shelli"
            """

second_query = """
                  UPDATE employees
                  SET first_name ="Sherry"
                  WHERE first_name = "Shelli"
               """
insert_and_delete(first_query,second_query)