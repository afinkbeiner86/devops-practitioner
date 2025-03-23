"""
a) Create a Student class

with properties:

first name
last name
age
lectures he/she attends
with methods:

can print the full name
can list the lectures, which the student attends
can add new lectures to the lectures list (attend a new lecture)
can remove lectures from the lectures list (leave a lecture)
"""
from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, lectures) -> None:
        super().__init__(first_name, last_name, age)
        self.lectures = lectures
 
    def print_lectures(self):
        print(f"Attending Lectures:")
        for lecture in self.lectures:
            print(f"- {lecture}")

    def attend_lecture(self, lecture_to_add):
        self.lectures.add(lecture_to_add)

    def leave_lecture(self, lecture_to_remove):
        self.lectures.remove(lecture_to_remove)