def add_numbers(number_one, number_two):
    return number_one + number_two
    
def substract_numbers(number_one, number_two):
    return number_one - number_two

def multiply_numbers(number_one, number_two):
    return number_one * number_two

def divide_numbers(number_one, number_two):
    return number_one / number_two

def validate_user_input(number_one, number_two):
    try:
        float(number_one)
        float(number_two)
    except ValueError:
        print('Invalid data type. Accepted numbers: integer and float.')

def validate_input_format(list_index):
    if list_index < 3:
        raise ValueError('Invalid input format. Accepted format: "10 + 20"')

def identify_operand(math_operand):
    if math_operand == "+":
        return(math_operand)
    elif math_operand == "-":
        return(math_operand)
    elif math_operand == "*":
        return(math_operand)
    elif math_operand == "/":
        return(math_operand)
    else:
        raise ValueError("Invalid math operand. Valid values are: + - * /")