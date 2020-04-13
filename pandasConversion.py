# populate the URL JSON data into a Pandas Dataframe
import requests
import pandas as pd

url = 'http://dummy.restapiexample.com/api/v1/employees'

r = requests.get(url)
packages_json = r.json()

employee_pd = pd.DataFrame.from_dict(packages_json['data'])
employee_pd.to_csv('employee_PD.csv', index=False)
