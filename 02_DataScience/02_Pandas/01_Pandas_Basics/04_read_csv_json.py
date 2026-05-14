# =========================================================
# Pandas Read CSV & JSON Tutorial
# Beginner to Advanced
# File: 04_read_csv_json.py
# =========================================================

# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS CSV?
# =========================================================

"""
CSV = Comma Separated Values

- Most common file format in Data Science
- Stores tabular data
- Used in:
    - Machine Learning
    - Data Analysis
    - Business Analytics

Example:

Name,Age,City
Mohit,22,Delhi
Aman,24,Noida
"""

print("========== CSV FILES ==========\n")


# =========================================================
# 3. READ CSV FILE
# =========================================================

print("========== READ CSV ==========\n")

# Sample:
# df = pd.read_csv("datasets/employees.csv")

# Uncomment when dataset exists

# print(df)

print("Syntax:")
print('pd.read_csv("file_path.csv")')

print("\n")


# =========================================================
# 4. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Rahul"],
    "Age": [22, 24, 23, 25],
    "City": ["Delhi", "Noida", "Mumbai", "Pune"],
    "Salary": [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 5. SAVE DATAFRAME AS CSV
# =========================================================

print("========== SAVE CSV ==========\n")

# Save CSV file
# df.to_csv("employees.csv", index=False)

print("CSV File Saved Successfully")

print("\n")


# =========================================================
# 6. READ ONLY FIRST ROWS
# =========================================================

print("========== HEAD() ==========\n")

print(df.head())

print("\n")


# =========================================================
# 7. READ LAST ROWS
# =========================================================

print("========== TAIL() ==========\n")

print(df.tail())

print("\n")


# =========================================================
# 8. CHECK DATA TYPES
# =========================================================

print("========== DATA TYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 9. INFO()
# =========================================================

print("========== INFO ==========\n")

print(df.info())

print("\n")


# =========================================================
# 10. SHAPE
# =========================================================

print("========== SHAPE ==========\n")

print(df.shape)

print("\n")


# =========================================================
# 11. READ SPECIFIC COLUMNS
# =========================================================

print("========== SPECIFIC COLUMNS ==========\n")

# Example syntax
# df = pd.read_csv(
#     "employees.csv",
#     usecols=["Name", "Salary"]
# )

print(df[["Name", "Salary"]])

print("\n")


# =========================================================
# 12. SKIP ROWS
# =========================================================

print("========== SKIP ROWS ==========\n")

"""
Syntax:

pd.read_csv(
    "file.csv",
    skiprows=2
)
"""

print("skiprows used to skip rows while reading")

print("\n")


# =========================================================
# 13. HANDLE MISSING VALUES
# =========================================================

print("========== HANDLE MISSING VALUES ==========\n")

data2 = {
    "Name": ["Mohit", "Aman", None, "Neha"],
    "Marks": [90, None, 85, 95]
}

missing_df = pd.DataFrame(data2)

print(missing_df)

print("\nNull Values:\n")

print(missing_df.isnull())

print("\n")


# =========================================================
# 14. FILL MISSING VALUES
# =========================================================

print("========== FILL MISSING VALUES ==========\n")

filled_df = missing_df.fillna(0)

print(filled_df)

print("\n")


# =========================================================
# 15. DROP NULL VALUES
# =========================================================

print("========== DROP NULL VALUES ==========\n")

dropped_df = missing_df.dropna()

print(dropped_df)

print("\n")


# =========================================================
# 16. CHANGE COLUMN NAMES
# =========================================================

print("========== CHANGE COLUMN NAMES ==========\n")

df.columns = ["Employee", "EmployeeAge", "EmployeeCity", "EmployeeSalary"]

print(df)

print("\n")


# =========================================================
# 17. READ LARGE DATASETS
# =========================================================

print("========== LARGE DATASETS ==========\n")

"""
Useful parameters:

nrows=
chunksize=
low_memory=
"""

print("Used for handling very large datasets")

print("\n")


# =========================================================
# 18. WHAT IS JSON?
# =========================================================

"""
JSON = JavaScript Object Notation

- Common format for APIs
- Widely used in web applications
- Stores data in key-value format
"""

print("========== JSON FILES ==========\n")


# =========================================================
# 19. READ JSON FILE
# =========================================================

print("========== READ JSON ==========\n")

# Example:
# df = pd.read_json("datasets/data.json")

print('Syntax: pd.read_json("file.json")')

print("\n")


# =========================================================
# 20. CREATE DATAFRAME FROM DICTIONARY
# =========================================================

print("========== DATAFRAME FROM DICTIONARY ==========\n")

json_data = {
    "Name": {
        "0": "Mohit",
        "1": "Aman",
        "2": "Neha"
    },
    "Marks": {
        "0": 90,
        "1": 85,
        "2": 95
    },
    "City": {
        "0": "Delhi",
        "1": "Noida",
        "2": "Mumbai"
    }
}

json_df = pd.DataFrame(json_data)

print(json_df)

print("\n")


# =========================================================
# 21. SAVE JSON FILE
# =========================================================

print("========== SAVE JSON ==========\n")

# json_df.to_json("students.json")

print("JSON File Saved Successfully")

print("\n")


# =========================================================
# 22. CONVERT CSV TO JSON
# =========================================================

print("========== CSV TO JSON ==========\n")

"""
Syntax:

df.to_json("data.json")
"""

print("CSV converted to JSON")

print("\n")


# =========================================================
# 23. CONVERT JSON TO CSV
# =========================================================

print("========== JSON TO CSV ==========\n")

"""
Syntax:

df.to_csv("data.csv")
"""

print("JSON converted to CSV")

print("\n")


# =========================================================
# 24. READ EXCEL FILE
# =========================================================

print("========== READ EXCEL ==========\n")

"""
Syntax:

pd.read_excel("file.xlsx")
"""

print("Excel file reading supported")

print("\n")


# =========================================================
# 25. EXPORT TO EXCEL
# =========================================================

print("========== EXPORT TO EXCEL ==========\n")

"""
Syntax:

df.to_excel("output.xlsx")
"""

print("Excel file exported")

print("\n")


# =========================================================
# 26. READ TEXT FILE
# =========================================================

print("========== READ TEXT FILE ==========\n")

"""
Syntax:

pd.read_table("file.txt")
"""

print("Text files can also be read")

print("\n")


# =========================================================
# 27. CHECK DUPLICATES
# =========================================================

print("========== DUPLICATES ==========\n")

duplicate_data = {
    "Name": ["A", "B", "B", "C"],
    "Marks": [90, 80, 80, 70]
}

duplicate_df = pd.DataFrame(duplicate_data)

print(duplicate_df)

print("\nDuplicate Rows:\n")

print(duplicate_df.duplicated())

print("\n")


# =========================================================
# 28. REMOVE DUPLICATES
# =========================================================

print("========== REMOVE DUPLICATES ==========\n")

clean_df = duplicate_df.drop_duplicates()

print(clean_df)

print("\n")


# =========================================================
# 29. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

employee_data = {
    "Name": ["Rahul", "Mohit", "Neha", "Aman"],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 70000, 55000]
}

employee_df = pd.DataFrame(employee_data)

print(employee_df)

print("\n")

print("Employees in IT Department:\n")

it_employees = employee_df[
    employee_df["Department"] == "IT"
]

print(it_employees)

print("\n")

print("Average Salary:\n")

print(employee_df["Salary"].mean())

print("\n")


# =========================================================
# 30. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What is CSV?

A file format used to store tabular data.

--------------------------------------------------

Q2. How to read CSV file?

Using:
pd.read_csv()

--------------------------------------------------

Q3. How to read JSON file?

Using:
pd.read_json()

--------------------------------------------------

Q4. How to save DataFrame as CSV?

Using:
df.to_csv()

--------------------------------------------------

Q5. How to handle missing values?

Using:
fillna()
dropna()

--------------------------------------------------

Q6. How to remove duplicate rows?

Using:
drop_duplicates()

--------------------------------------------------

Q7. How to read Excel files?

Using:
pd.read_excel()

--------------------------------------------------

Q8. Why is CSV important in ML?

Because datasets are mostly stored in CSV format.
"""

# =========================================================
# 31. END OF FILE
# =========================================================

print("========== CSV & JSON TUTORIAL COMPLETED ==========")