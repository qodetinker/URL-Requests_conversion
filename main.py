import requests
import sqlite3

url = 'http://dummy.restapiexample.com/api/v1/employees'

r = requests.get(url)
packages_json = r.json()

# Create the employee database if it does not exist
db = sqlite3.connect('employee.sqlite')
#create the table
db.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMAR KEY, employee_name TEXT, employee_salary INTEGER, employee_age INTEGER, profile_image BLOB)")
#db.execute("INSERT INTO employee(id, employee_name, employee_salary, employee_age, profile_image) VALUES(1, 'Levi', 50000, 24, '')")

# Loop through each employee information and insert into database
for employee in packages_json['data']:
    db.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?)", [employee["id"], employee["employee_name"], employee["employee_salary"], employee["employee_age"],employee["profile_image"]])
    db.commit()
db.close()
