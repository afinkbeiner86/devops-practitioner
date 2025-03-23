"""
EXERCISE 7: Working with Classes and Objects
Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects:
"""

from student import Student
from professor import Professor
from lecture import Lecture

student_one = Student("Bob", "Ross", 36, {"Art", "Math"})
student_one.print_full_name()
student_one.print_lectures()

student_one.attend_lecture("Design")
student_one.print_lectures()

student_one.leave_lecture("Math")
student_one.print_lectures()

professor_one = Professor("Albert", "Einstein", 70, {"Physics", "Math"})
professor_one.print_full_name()
professor_one.print_subjects()

professor_one.add_subject("Astro Physics")
professor_one.print_subjects()

professor_one.remove_subject("Math")
professor_one.print_subjects()

lecture_math = Lecture("Math", 60, 120, {"Albert Einstein", "Professor Dumbledore"})
lecture_math.print_name()
lecture_math.print_duration()
lecture_math.print_professors_teaching()
lecture_math.remove_professor("Professor Dumbledore")
lecture_math.print_professors_teaching()