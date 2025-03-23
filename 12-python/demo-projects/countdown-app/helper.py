user_input_message = "Convert days to minutes or hours like so:  30:minutes.\n"

def days_to_units(number_of_days, name_of_unit):
    if name_of_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} {name_of_unit}"
    elif name_of_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} {name_of_unit}"
    else:
        return f"Unit not supported. Supported units: minutes, hours."

def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number < 0:
            print("You entered a negative value.")
        elif user_input_number == 0:
            print("You entered 0 as value.")
        else:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
    except ValueError:
        print("Your input is a non-integer value.")