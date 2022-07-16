

import mysql.connector
from config import get_database

def concat_emp_to_mgr(query):
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

# write a SQL query to find the name of employees and their manager separated by the string 'works for'

concat_query ="""
                        SELECT CONCAT (e.emp_name," works for ", m.emp_name) AS 'employee TO manager'
                        FROM employees e
                        INNER JOIN employees m
                        ON e.manager_id = m.emp_id;
                        """


concat_emp_to_mgr(concat_query)
'''
('SANDRINE works for FRANK',)
('ADELYN works for BLAZE',)
('WADE works for BLAZE',)
('JONAS works for KAYLING',)
('MADDEN works for BLAZE',)
('BLAZE works for KAYLING',)
('CLARE works for KAYLING',)
('SCARLET works for JONAS',)
('TUCKER works for BLAZE',)
('ADNRES works for SCARLET',)
('JULIUS works for BLAZE',)
('FRANK works for JONAS',)
('MARKER works for CLARE',)
'''