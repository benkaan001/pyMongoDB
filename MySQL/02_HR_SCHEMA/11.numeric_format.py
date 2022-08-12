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


three_digit_seperated= """
        SELECT FORMAT(9999999, 'N', 'en-us') AS 'Number'
        """

# ('9,999,999',)

format(three_digit_seperated)