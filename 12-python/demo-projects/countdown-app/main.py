from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    try:
        if user_input == "exit":
            print("User exited.")
            raise SystemExit()
        elif user_input.strip() == '':
            print("User input empty.")
        else:
            days_and_unit = user_input.split(":")
            days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
            validate_and_execute(days_and_unit_dictionary)
    except ValueError:
        print("User input invalid.")
