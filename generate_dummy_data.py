from faker import Faker
import pandas as pd
import random

TARGET_ROW_NUM = 100

# generate data based on US and GB locale
fake = Faker(["en_US", "en_GB"])

employees = []

for _ in range(TARGET_ROW_NUM + 1):
    # create id
    emp_id = fake.pyint(min_value=1, max_value=1000, step=1)
    # create first name
    emp_first_name = fake.first_name()
    # create last name
    emp_last_name = fake.last_name()
    # create hire date - default from 1/1/1970 to today
    emp_hire_date = fake.date()
    # create salary
    emp_salary = fake.pyint(min_value=40000, max_value=250000, step=5000)
    # create email
    emp_email = fake.ascii_email()
    # create basic bank account number - ie 'MYNB48...'
    emp_bank_acct_no = fake.bban()
    # create gender
    emp_gender = random.choice(["M", "F", "Other"])
    # create language
    emp_lang = fake.locale()
    # create SSN
    emp_ssn = fake.ssn()
    # create address
    emp_address = fake.address()

    employees.append(
        [
            emp_id,
            emp_first_name,
            emp_last_name,
            emp_hire_date,
            emp_salary,
            emp_email,
            emp_bank_acct_no,
            emp_gender,
            emp_lang,
            emp_ssn,
            emp_address,
        ]
    )
col = [
    "emp_id",
    "emp_first_name",
    "emp_last_name",
    "emp_hire_date",
    "emp_salary",
    "emp_email",
    "emp_bank_acct_no",
    "emp_gender",
    "emp_lang",
    "emp_ssn",
    "emp_address",
]
employees_df = pd.DataFrame(employees, columns=col)
path = "/Users/benkaan/Desktop/pyMongoDB/dummy_employee_data.csv"
try:
    employees_df.to_csv(
        rf"{path}", index=False, sep=",", encoding="utf-8", date_format="%Y-%m-%d"
    )
except Exception as e:
    print(e)
else:
    print(f"File crated successfully at {path}")
    print(employees_df)
