import mysql.connector
from config import get_database

def get_conditional_bonus(query):
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

# Multi conditional bonus
# Formatted 000,000
conditional_bonus_query = """
            SELECT j.job_title, e.first_name, e.salary,
            CASE
	            WHEN job_title LIKE('%Manager%') AND salary < 10000 THEN CONVERT(FORMAT((salary * 0.2), 'N', 'en-us'),CHAR)
                WHEN job_title LIKE('%Clerk%') THEN CONVERT(FORMAT((salary * 0.3), 'N', 'en-us'),CHAR)
                WHEN job_title LIKE('%Clert%') AND salary < 3000 THEN CONVERT(FORMAT((salary * 0.5), 'N','en-us'), CHAR)
	            ELSE 'Come Back Next Year'
            END bonus
            FROM jobs j
            INNER JOIN employees e
            ON e.job_id = j.job_id
            """


get_conditional_bonus(conditional_bonus_query)
