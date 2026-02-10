import json
from student import Student

FILE_PATH = "data/students.json"


def load_students():
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return [Student(d["sid"], d["name"], d["marks"]) for d in data]
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_PATH, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)
