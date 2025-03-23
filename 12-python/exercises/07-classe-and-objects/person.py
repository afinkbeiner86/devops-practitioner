"""
d) Bonus task

As both students and professors have a first name, last name and age, you think of a cleaner solution:

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Create a Person class, which is the parent class of Student and Professor classes
This Person class has the following properties: "first_name", "last_name" and "age"
and following method: "print_name", which can print the full name
So you don't need these properties and method in the other two classes. You can easily inherit these.
Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class"""

class Person:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def print_full_name(self):
        print(f"Full name: {self.first_name} {self.last_name}")

    def print_age(self):
        print(f"Age: {self.age}")