"""
Write a function that accepts a list of dictionaries with employee age (see example list from the Exercise 3) and prints out the name and age of the youngest employee.
Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
Write a function that prints the even numbers from a provided list.
For cleaner code, declare these functions in its own helper Module and use them in the main.py file
"""
# Write a function that accepts a list of dictionaries with employee age (see example list from the Exercise 3) and prints out the name and age of the youngest employee.
def print_youngest_employee(employees_list):
    employee_ages = []
    for employee in employees_list:
        employee_ages.append(employee.get("age"))
        employee_min_age = min(employee_ages)

    for employee in employees_list:
        if employee["age"] == employee_min_age:
            youngest_employee_name = employee["name"]
            youngest_employee_age = employee["age"]
            print(f"Youngest employee:\n Name: {youngest_employee_name}\n Age: {youngest_employee_age}")

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
def calculate_upper_lower_case(input_string):
    letter_list = []
    lower_case_letters = 0
    upper_case_letters = 0
    
    for letter in input_string:
        letter_list.append(letter)
    
    for letter in letter_list:
        if letter.isupper() == True:
            upper_case_letters = upper_case_letters + 1
        else:
            lower_case_letters = lower_case_letters + 1
    
    print(f"The input string contains {lower_case_letters} lower and {upper_case_letters} upper case letters.")

# Write a function that prints the even numbers from a provided list
def print_even_numbers(input_numbers):
    even_numbers = []
    for number in input_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(f"Even numbers: {even_numbers}")