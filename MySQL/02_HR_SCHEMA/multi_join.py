import mysql.connector
from config import get_database

def get_reps(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print("FirstName:",record[0], " \tSalary:",record[1], "\tDeptID:",record[2], "\tDeptName:", record[3],"\tTitle:",record[4])
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

# display first_name, salary, department_id, department_name, and job_title of all employees
# who have "Representative" in their job titles
reps_query ="""
            SELECT e.first_name, e.salary, e.department_id, d.department_name, j.job_title
            FROM employees e
            INNER JOIN jobs j
            ON e.job_id = j.job_id
            LEFT JOIN departments d
            ON d.department_id = e.department_id
            WHERE j.job_title LIKE '%Representative%'
            """


get_reps(reps_query)
# notice that Kimberly does not have a dept ID though she is a Sales Rep. A second inner join would have left her out.
"""
FirstName: Susan        Salary: 6500.00         DeptID: 40      DeptName: Human Resources       Title: Human Resources Representative
FirstName: Pat          Salary: 6000.00         DeptID: 20      DeptName: Marketing     Title: Marketing Representative
FirstName: Hermann      Salary: 10000.00        DeptID: 70      DeptName: Public Relations      Title: Public Relations Representative
FirstName: Peter        Salary: 10000.00        DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: David        Salary: 9500.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Peter        Salary: 9000.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Christopher  Salary: 8000.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Nanette      Salary: 7500.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Oliver       Salary: 7000.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Janette      Salary: 10000.00        DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Patrick      Salary: 9500.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Allan        Salary: 9000.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Lindsey      Salary: 8000.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Louise       Salary: 7500.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Sarath       Salary: 7000.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Clara        Salary: 10500.00        DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Danielle     Salary: 9500.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Mattea       Salary: 7200.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: David        Salary: 6800.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Sundar       Salary: 6400.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Amit         Salary: 6200.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Lisa         Salary: 11500.00        DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Harrison     Salary: 10000.00        DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Tayler       Salary: 9600.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: William      Salary: 7400.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Elizabeth    Salary: 7300.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Sundita      Salary: 6100.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Ellen        Salary: 11000.00        DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Alyssa       Salary: 8800.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Jonathon     Salary: 8600.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Jack         Salary: 8400.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
FirstName: Kimberely    Salary: 7000.00         DeptID: None    DeptName: None          Title: Sales Representative
FirstName: Charles      Salary: 6200.00         DeptID: 80      DeptName: Sales         Title: Sales Representative
"""

def get_job_title_only(query):
    connection=get_database()
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        for record in records:
            print("FirstName:",record[0], "\tTitle:",record[1])
        connection.commit()
    except mysql.connector.Error as error:
        print(f".......ERROR....{error}")
    finally:
        cursor.close()
        connection.close()
        print(".......Connection closed SUCCESSFULLY!")

query = """
        SELECT e.first_name, j.job_title
        FROM employees e
        INNER JOIN jobs j
        ON e.job_id = j.job_id
        WHERE j.job_title LIKE '%Representative%'
        """

get_job_title_only(query)

"""
.
.
.
FirstName: Kimberely    Title: Sales Representative
FirstName: Charles      Title: Sales Representative
"""