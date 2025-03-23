"""
Write a Python Script that:
- Updates the job to Software Engineer
- Removes the age key from the dictionary
- Loops through the dictionary and prints the key:value pairs one by one
"""

employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Update the job to Software Engineer
employee.update({"job":"Software Engineer"})
print(f"{employee}\n---")

# Remove the age key from the dictionary
employee.__delitem__("age")
print(f"{employee}\n---")

# Loop through the dictionary and prints the key:value pairs one by one

for key, value in employee.items():
  print(f"{key}:{value}")

#for key_value in employee:
#    key_value_pair = employee.get(key_value)
#    print(f"{key_value}: {key_value_pair}")

print("---")

"""
Write a Python Script that:
- Merges these two Python dictionaries into 1 new dictionary.
- Sums up all the values in the new dictionary and print it out
- Prints the max and minimum values of the dictionary
"""


dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

# Merge these two Python dictionaries into 1 new dictionary
dict_three = dict_one.copy()
dict_three.update(dict_two)
print(f"{dict_three}\n---")

# Sums up all the values in the new dictionary and print it out
value_sum = 0
for key in dict_three:
    value_sum = value_sum + dict_three.get(key)
print(f"{value_sum}\n---")

# Print the max and minimum values of the dictionary
all_values = dict_three.values()
min_value = min(all_values)
max_value = max(all_values)
print(min_value)
print(max_value)