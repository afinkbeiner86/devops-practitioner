from helper import print_youngest_employee, calculate_upper_lower_case, print_even_numbers

# For cleaner code, declare these functions in its own helper Module and use them in the main.py file
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

numbers_list = [1,2,3,4,5,6,7,8,10]

print_youngest_employee(employees)
calculate_upper_lower_case("teStTesTEtSt")
print_even_numbers(numbers_list)