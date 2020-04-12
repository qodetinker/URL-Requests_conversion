# populate the URL JSON data into a CSV
import requests
import csv

url = 'http://dummy.restapiexample.com/api/v1/employees'

r = requests.get(url)
packages_json = r.json()

columns = ['id', 'employee_name', 'employee_salary', 'employee_age', 'profile_image']

# Loop through each employee information and insert into database
with open('employee.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for employee in packages_json['data']:
        writer.writerow(employee)
        print(employee)