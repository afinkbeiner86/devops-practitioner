"""
b) Create a Professor class

with properties:

first name
last name
age
subjects he/she teaches
with methods:

can print the full name
can list the subjects they teach
can add new subjects to the list
can remove subjects from the list"""
from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, subjects) -> None:
        super().__init__(first_name, last_name, age)
        self.subjects = subjects

    def print_subjects(self):
        print(f"Teaching Subjects:")
        for subjects in self.subjects:
            print(f"- {subjects}")

    def add_subject(self, subject_to_add):
        self.subjects.add(subject_to_add)

    def remove_subject(self, subject_to_remove):
        self.subjects.remove(subject_to_remove)