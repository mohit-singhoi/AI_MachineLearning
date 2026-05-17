# =========================================================
# Pandas Data Type Conversion Tutorial
# Beginner to Advanced
# File: 03_data_type_conversion.py
# Folder: 02_Data_Cleaning
# =========================================================


# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS DATA TYPE CONVERSION?
# =========================================================

"""
Data Type Conversion means:

Changing one data type into another.

Examples:
- String → Integer
- Float → Integer
- Integer → Float
- Object → Datetime
- Object → Category

Why Important?

- Reduces memory usage
- Improves performance
- Required for Machine Learning
- Helps in calculations

Common Functions:
- astype()
- to_numeric()
- to_datetime()
"""

print("========== DATA TYPE CONVERSION ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Simran"],
    "Age": ["22", "25", "23", "26"],
    "Salary": ["50000", "65000", "55000", "70000"],
    "PerformanceScore": [85.5, 90.2, 88.7, 91.5],
    "JoiningDate": [
        "2023-01-15",
        "2022-07-10",
        "2021-05-20",
        "2020-03-11"
    ]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. CHECK DATA TYPES
# =========================================================

print("========== DATA TYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 5. CONVERT STRING TO INTEGER
# =========================================================

print("========== STRING TO INTEGER ==========\n")

df["Age"] = df["Age"].astype(int)

print(df)

print("\n")

print(df.dtypes)

print("\n")


# =========================================================
# 6. CONVERT STRING TO FLOAT
# =========================================================

print("========== STRING TO FLOAT ==========\n")

df["Salary"] = df["Salary"].astype(float)

print(df)

print("\n")

print(df.dtypes)

print("\n")


# =========================================================
# 7. CONVERT FLOAT TO INTEGER
# =========================================================

print("========== FLOAT TO INTEGER ==========\n")

df["PerformanceScore"] = (
    df["PerformanceScore"].astype(int)
)

print(df)

print("\n")

print(df.dtypes)

print("\n")


# =========================================================
# 8. CONVERT INTEGER TO FLOAT
# =========================================================

print("========== INTEGER TO FLOAT ==========\n")

df["Age"] = df["Age"].astype(float)

print(df)

print("\n")

print(df.dtypes)

print("\n")


# =========================================================
# 9. CONVERT USING to_numeric()
# =========================================================

print("========== TO_NUMERIC ==========\n")

salary_series = pd.to_numeric(
    df["Salary"]
)

print(salary_series)

print("\n")


# =========================================================
# 10. HANDLE INVALID CONVERSION
# =========================================================

print("========== INVALID CONVERSION ==========\n")

invalid_data = pd.DataFrame({
    "Marks": ["90", "85", "Absent", "70"]
})

print("ORIGINAL DATA:\n")

print(invalid_data)

print("\n")

invalid_data["Marks"] = pd.to_numeric(
    invalid_data["Marks"],
    errors="coerce"
)

print("AFTER CONVERSION:\n")

print(invalid_data)

print("\n")


# =========================================================
# 11. CONVERT TO BOOLEAN
# =========================================================

print("========== BOOLEAN CONVERSION ==========\n")

data2 = {
    "Result": [1, 0, 1, 1]
}

bool_df = pd.DataFrame(data2)

bool_df["Result"] = bool_df["Result"].astype(bool)

print(bool_df)

print("\n")

print(bool_df.dtypes)

print("\n")


# =========================================================
# 12. CONVERT TO CATEGORY
# =========================================================

print("========== CATEGORY CONVERSION ==========\n")

df["Name"] = df["Name"].astype("category")

print(df.dtypes)

print("\n")


# =========================================================
# 13. CONVERT TO DATETIME
# =========================================================

print("========== DATETIME CONVERSION ==========\n")

df["JoiningDate"] = pd.to_datetime(
    df["JoiningDate"]
)

print(df)

print("\n")

print(df.dtypes)

print("\n")


# =========================================================
# 14. EXTRACT YEAR FROM DATETIME
# =========================================================

print("========== EXTRACT YEAR ==========\n")

df["JoiningYear"] = (
    df["JoiningDate"].dt.year
)

print(df)

print("\n")


# =========================================================
# 15. EXTRACT MONTH
# =========================================================

print("========== EXTRACT MONTH ==========\n")

df["JoiningMonth"] = (
    df["JoiningDate"].dt.month
)

print(df)

print("\n")


# =========================================================
# 16. EXTRACT DAY
# =========================================================

print("========== EXTRACT DAY ==========\n")

df["JoiningDay"] = (
    df["JoiningDate"].dt.day
)

print(df)

print("\n")


# =========================================================
# 17. MEMORY USAGE
# =========================================================

print("========== MEMORY USAGE ==========\n")

print(df.memory_usage())

print("\n")


# =========================================================
# 18. MEMORY OPTIMIZATION
# =========================================================

print("========== MEMORY OPTIMIZATION ==========\n")

optimized_df = pd.DataFrame({
    "Category": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "HR"
    ]
})

print("BEFORE:\n")

print(
    optimized_df["Category"].dtype
)

print("\n")

optimized_df["Category"] = (
    optimized_df["Category"].astype("category")
)

print("AFTER:\n")

print(
    optimized_df["Category"].dtype
)

print("\n")


# =========================================================
# 19. MULTIPLE COLUMN CONVERSION
# =========================================================

print("========== MULTIPLE COLUMN CONVERSION ==========\n")

multi_df = pd.DataFrame({
    "Math": ["90", "85", "88"],
    "Science": ["80", "92", "89"]
})

print("BEFORE:\n")

print(multi_df.dtypes)

print("\n")

multi_df = multi_df.astype(int)

print("AFTER:\n")

print(multi_df.dtypes)

print("\n")


# =========================================================
# 20. APPLY FUNCTION CONVERSION
# =========================================================

print("========== APPLY FUNCTION ==========\n")

apply_df = pd.DataFrame({
    "Salary": [50000, 60000, 70000]
})

apply_df["Salary"] = (
    apply_df["Salary"].apply(float)
)

print(apply_df)

print("\n")

print(apply_df.dtypes)

print("\n")


# =========================================================
# 21. LAMBDA CONVERSION
# =========================================================

print("========== LAMBDA CONVERSION ==========\n")

lambda_df = pd.DataFrame({
    "Age": ["22", "25", "28"]
})

lambda_df["Age"] = lambda_df["Age"].apply(
    lambda x: int(x)
)

print(lambda_df)

print("\n")

print(lambda_df.dtypes)

print("\n")


# =========================================================
# 22. CONVERT OBJECT TO STRING
# =========================================================

print("========== OBJECT TO STRING ==========\n")

object_df = pd.DataFrame({
    "Code": [101, 102, 103]
})

object_df["Code"] = (
    object_df["Code"].astype(str)
)

print(object_df)

print("\n")

print(object_df.dtypes)

print("\n")


# =========================================================
# 23. CHECK FINAL DATA TYPES
# =========================================================

print("========== FINAL DATA TYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 24. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {
    "Student": ["Rahul", "Mohit", "Neha"],
    "Math": ["90", "85", "95"],
    "Science": ["88", "91", "89"],
    "JoinDate": [
        "2023-01-01",
        "2022-06-15",
        "2021-08-20"
    ]
}

students_df = pd.DataFrame(student_data)

print("ORIGINAL DATA:\n")

print(students_df)

print("\n")

print("ORIGINAL DTYPES:\n")

print(students_df.dtypes)

print("\n")

students_df["Math"] = (
    students_df["Math"].astype(int)
)

students_df["Science"] = (
    students_df["Science"].astype(int)
)

students_df["JoinDate"] = pd.to_datetime(
    students_df["JoinDate"]
)

print("UPDATED DATA:\n")

print(students_df)

print("\n")

print("UPDATED DTYPES:\n")

print(students_df.dtypes)

print("\n")


# =========================================================
# 25. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Data Type Conversion is extremely
important in Data Cleaning.

Real-world datasets often contain:
- Numeric values stored as strings
- Invalid values
- Incorrect date formats

Common Industry Usage:
- Machine Learning
- ETL Pipelines
- Data Warehousing
- Financial Analysis

Benefits:
- Faster computation
- Better memory usage
- Accurate calculations
"""

print("Data Type Conversion Is Industry Critical")

print("\n")


# =========================================================
# 26. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What is data type conversion?

Ans:
Changing one datatype into another.

--------------------------------------------------

Q2. Which function is commonly used?

Using:
astype()

--------------------------------------------------

Q3. How to convert string to integer?

Using:
astype(int)

--------------------------------------------------

Q4. How to convert string to datetime?

Using:
pd.to_datetime()

--------------------------------------------------

Q5. What does errors='coerce' do?

Ans:
Invalid values become NaN.

--------------------------------------------------

Q6. Why category datatype is useful?

Ans:
It reduces memory usage.

--------------------------------------------------

Q7. Why datatype conversion is important?

Ans:
For:
- Calculations
- Machine Learning
- Performance optimization

--------------------------------------------------

Q8. Difference between astype() and to_numeric()?

astype():
Direct conversion

to_numeric():
Handles invalid values better
"""


# =========================================================
# 27. END OF FILE
# =========================================================

print("========== DATA TYPE CONVERSION COMPLETED ==========")