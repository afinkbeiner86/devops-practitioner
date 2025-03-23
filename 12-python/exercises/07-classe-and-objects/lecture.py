"""
c) Create a Lecture class

with properties:

name
max number of students
duration
list of professors giving this lecture
with methods:

printing the name and duration of the lecture
adding professors to the list of professors giving this lecture
"""

class Lecture:
    def __init__(self, name, max_attendees, duration, professors_teaching) -> None:
        self.name = name
        self.max_attendees = max_attendees
        self.duration = duration
        self.professors_teaching = professors_teaching

    def print_name(self):
        print(f"Lecture name: {self.name}")
    
    def print_duration(self):
        print(f"Duration: {self.duration} min")

    def print_professors_teaching(self):
        print(f"Professors teaching:")
        for professor in self.professors_teaching:
            print(f"- {professor}")
    
    def add_professor(self, professor_to_add):
        self.professors_teaching.add(professor_to_add)
    
    def remove_professor(self, professors_to_remove):
        self.professors_teaching.remove(professors_to_remove)