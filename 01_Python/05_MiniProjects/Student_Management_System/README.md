# 🎓 Student Management System (Python – OOPS Based)

## 📌 Project Overview
The **Student Management System** is a menu-driven Python project that manages student records using **Object-Oriented Programming (OOPS)** concepts and **JSON file handling**.

It allows users to:
- Add new students  
- View existing students  
- Update student marks  
- Store data permanently in a JSON file  

This project is beginner-friendly and suitable for **college projects, viva, and resumes**.

---

## 🗂 Project Structure



Student_Management_System/
│
├── main.py
├── student.py
├── file_manager.py
├── exceptions.py
│
└── data/
└── students.json


---

## 📄 File Explanation

### 1️⃣ `student.py` (Student Blueprint)
This file defines what a **Student** is.

- Stores student details (ID, Name, Marks)
- Calculates grade automatically
- Uses OOPS concepts:
  - Encapsulation
  - Inheritance
  - Abstraction
  - Polymorphism

This file **does not run the program**.

---

### 2️⃣ `file_manager.py` (File Handling Layer)
This file handles **reading and writing data**.

- Reads student data from `students.json`
- Converts JSON data into Student objects
- Saves updated student data back to JSON

Think of this as a **data storage manager**.

---

### 3️⃣ `main.py` (Main Controller)
This is the **main executable file**.

- Displays menu
- Takes user input
- Calls functions from other files
- Controls program flow

This file connects everything together.

---

### 4️⃣ `students.json` (Database)
This file stores student records permanently.

- Data remains even after program exits
- Acts like a simple database

Example:
```json
{
  "sid": "S001",
  "name": "Aarav Sharma",
  "marks": 85
}

🔄 Project Workflow (Step-by-Step)
▶️ Step 1: Program Starts

User runs main.py

Existing students are loaded from students.json

▶️ Step 2: Menu Displayed
1. Add Student
2. View Students
3. Update Marks
4. Exit

▶️ Step 3: Add Student

User enters ID, name, and marks

Student object is created

Data is saved to JSON file

▶️ Step 4: View Students

Program reads all students

Displays student details with grade

▶️ Step 5: Update Marks

User enters student ID

Marks are updated

JSON file is updated permanently

▶️ Step 6: Exit

Program exits safely