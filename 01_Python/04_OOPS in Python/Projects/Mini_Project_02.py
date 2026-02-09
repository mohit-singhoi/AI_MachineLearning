# Student Management System

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.__marks = marks

    def update_marks(self, marks):
        self.__marks = marks

    def grade(self):
        if self.__marks >= 75:
            return "A"
        elif self.__marks >= 60:
            return "B"
        else:
            return "C"

    def display(self):
        print(self.roll, self.name, self.__marks, self.grade())


s1 = Student(1, "Mohit", 82)
s1.display()
s1.update_marks(90)
s1.display()
