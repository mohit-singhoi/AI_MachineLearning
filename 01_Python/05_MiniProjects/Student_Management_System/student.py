from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    @abstractmethod
    def display(self):
        pass


class Student(Person):
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.__marks = marks  # Encapsulation

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100")

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "Fail"

    def display(self):
        print(
            f"ID: {self.sid} | Name: {self.name} | Marks: {self.__marks} | Grade: {self.grade()}"
        )

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "marks": self.__marks
        }
