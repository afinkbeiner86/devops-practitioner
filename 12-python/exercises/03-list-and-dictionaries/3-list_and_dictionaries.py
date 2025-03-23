"""
Write a Python Program that:
Prints out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2.
Prints the country of the second employee in the list by accessing it directly without the loop.
"""

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

# Print out - the name, job and city of each employee using a loop. 
# The program must work for any number of employees in the list, not just 2.0

for employee in employees:
    employee_name = employee.get("name")
    employee_job = employee.get("job")
    employee_city = employee["address"].get("city")
    print(f"Name: {employee_name}\nJob: {employee_job}\nCity: {employee_city}\n---")

# Print the country of the second employee in the list
# by accessing it directly without the loop.

employee_country = employees[1]["address"].get("country")

print(f"Country of employee #2: {employee_country}")