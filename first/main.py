"""
class Student:
    def __init__(self, height=160):
        self.height=height

tim=Student()
andrey=Student(height=175)
print(tim.height)
print(andrey.height)
"""
class Student:
    amoung_of_students = 0
    def __init__(self, height=175):
        self.height=height
        Student.amoung_of_students += 1
        nick=Student()
        kate=Student(height=150)
        print(nick.amoung_of_students)
        print(Student.amoung_of_students)