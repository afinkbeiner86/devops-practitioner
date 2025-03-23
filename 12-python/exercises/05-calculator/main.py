"""
EXERCISE 5: Python Program 'Calculator'
Write a simple calculator program that:

takes user input of 2 numbers and operation to execute
handles following operations: plus, minus, multiply, divide
does proper user validation and give feedback: only numbers allowed
Keeps the Calculator program running until the user types “exit”
Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did

Concepts covered: working with different data types, conditionals, type conversion, user input, user input validation
"""

from calculator import *

user_input = ""
count_of_calculations = 0

while user_input != "exit":
    user_input = input('Enter calculation (accepted format: "10 + 20"): ')
    try:
        if user_input == "exit":
            print(f"User exited. Calculations done: {count_of_calculations}.")
            raise SystemExit()
        elif user_input.strip() == '':
            print("User input empty.")
        else:
            user_input_list = user_input.split()
            list_index = len(user_input_list)
            validate_input_format(list_index)
            validate_user_input(user_input_list[0], user_input_list[2])
            
            number_one = float(user_input_list[0])
            number_two = float(user_input_list[2])
            
            math_operand = user_input_list[1]
            math_operation = identify_operand(math_operand)
            
            if math_operation == "+":
                result = add_numbers(number_one, number_two)
            elif math_operation == "-":
                result = substract_numbers(number_one, number_two)
            elif math_operation == "*":
                result = multiply_numbers(number_one, number_two)
            elif math_operation == "/":
                result = divide_numbers(number_one, number_two)
            
            print(f"Result: {result}")
            count_of_calculations += 1
    except ValueError:
        print("User input invalid.")