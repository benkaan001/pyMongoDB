import mysql.connector
from config import get_database

def format(query):
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


format_query = """
            SELECT FORMAT(100500.5634, 2) AS 'NUM'
            """

format(format_query) # ('100,500.56',)
