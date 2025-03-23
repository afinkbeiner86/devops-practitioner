set_of_days = {"Monday", "Tuesday", "Wednesday"}
for day in set_of_days:
    print(day)
print("---\n")

set_of_days.add("Thursday")
for day in set_of_days:
    print(day)
print("---\n")

set_of_days.remove("Monday")
for day in set_of_days:
    print(day)
    