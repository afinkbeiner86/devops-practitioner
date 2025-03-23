"""
EXERCISE 8: Working with Dates
Write a program that:

accepts user's birthday as input
and calculates how many days, hours and minutes are remaining till the birthday
prints out the result as a message to the user"""

from datetime import datetime

user_input_birthday = input("Enter your birthday: ")

birthday_date = datetime.strptime(user_input_birthday, '%d.%m.%Y').date()

today = datetime.today().date()

if birthday_date > today:
    print("Woah, are you from the future?")
    raise SystemExit()

difference_one = datetime(today.year, birthday_date.month, birthday_date.day).date()
difference_two = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

days_till_birthday = 0

if difference_one == datetime.today().date():
    print("Today's your birthday! HAPPY BIRTHDAY!")
    raise SystemExit()
elif difference_one > today:
    # birthday this year
    days_till_birthday = difference_one - today
else:
    # birthday next year
    days_till_birthday = difference_two - today   

print(f"Days left unitl your birthday: {days_till_birthday.days}")


## First solution:

# this_year = int(today.strftime("%Y"))
# next_year = this_year + 1
# birthday = birthday.replace(year=this_year)

# if birthday < today:
#     birthday = birthday.replace(year=next_year)
#     birthday_today_delta = birthday - today
# else:
#     birthday_today_delta = birthday - today