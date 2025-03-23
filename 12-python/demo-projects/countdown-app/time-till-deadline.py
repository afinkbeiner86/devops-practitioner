import datetime

user_input = input("Enter your goal and deadline. Seperate with colon.\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
# input_dictionary = {"goal": input_list[0], "deadline": input_list[1]}

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_left = deadline_date - today_date
time_left_seconds = int(time_left.total_seconds() / 60)
unit = ""

if time_left_seconds < 60:
    time_left = int(time_left_seconds)
    unit = "second(s)"
elif time_left_seconds < 3600:
    time_left = int(time_left_seconds / 60)
    unit = "minute(s)"
elif time_left_seconds < 86400:
    time_left = int(time_left_seconds / 60 / 60)
    unit = "hour(s)"
else:
    time_left = int(time_left.days)
    unit = "day(s)"

print(f"Time remaining for goal: {goal}, {time_left} {unit}.")