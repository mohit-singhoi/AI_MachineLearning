from student import Student
from file_manager import load_students, save_students

class StudentNotFoundError(Exception):
    pass

students = load_students()

def find_student(sid):
    for s in students:
        if s.sid == sid:
            return s
    raise StudentNotFoundError("Student not found")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            sid = input("Student ID: ")
            name = input("Name: ")
            marks = int(input("Marks: "))
            s = Student(sid, name, marks)
            students.append(s)
            save_students(students)
            print("Student added successfully")

        elif choice == 2:
            if not students:
                print("No records found")
            for s in students:
                s.display()

        elif choice == 3:
            sid = input("Enter Student ID: ")
            student = find_student(sid)
            new_marks = int(input("Enter new marks: "))
            student.set_marks(new_marks)
            save_students(students)
            print("Marks updated")

        elif choice == 4:
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice")

    except ValueError as ve:
        print("Error:", ve)

    except StudentNotFoundError as se:
        print("Error:", se)

    except Exception as e:
        print("Unexpected Error:", e)
