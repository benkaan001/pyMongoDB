import mysql.connector
from config import get_database

"""

If multi is set to True, execute() is able to execute multiple statements specified in the query string.
It returns an iterator that enables processing the result of each statement.
"""

def fetch_records(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        for result in cursor.execute(query, multi=True):
            if result.with_rows:
                print("Rows produced by statement '{}':".format(result.statement))
                print(result.fetchall())
            else:
                print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))
        # cursor.execute(query, multi=True)
        # records = cursor.fetchall()
        # for record in records:
        #     print(record)
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

 #Write a query to fetch even numbered records from employees table.

even_numbered_id_query="""
                        SELECT  ROW_NUMBER() OVER() AS row_num,
                        employee_id, CONCAT(first_name, " ", last_name) name
                        FROM employees
                        WHERE MOD(employee_id,2) = 0
                        """
                        # WHERE (employee_id % 2) = 0
                        # WHERE (employee_id % 2) <> 0  for non-even

alternative_even_numbered_id_query = """
                                    SET @row_num =0;
                                    SELECT (@row_num:=@row_num+2) AS row_num,
                                    employee_id, CONCAT(first_name, " ", last_name) name
                                    FROM employees
                                    WHERE (employee_id % 2) = 0
                                    """


# fetch_records(even_numbered_id_query)
fetch_records(alternative_even_numbered_id_query)

"""
row_num	    employee_id	        name
2	        100	            Steven King
4	        102	            Lex De Haan
6	        104	            Bruce Ernst
8	        106	            Valli Pataballa
10	        108     	    Nancy Greenberg

"""