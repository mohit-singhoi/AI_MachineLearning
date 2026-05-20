# =========================================================
# Pandas Column Operations Tutorial
# Beginner to Advanced
# File: 06_column_operations.py
# =========================================================


# =========================================================
# 1. IMPORT LIBRARIES
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT ARE COLUMN OPERATIONS?
# =========================================================

"""
Column Operations means:

- Adding columns
- Updating columns
- Deleting columns
- Renaming columns
- Creating calculated columns

Very important in:
- Data Analysis
- Machine Learning
- Feature Engineering
"""

print("========== COLUMN OPERATIONS ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== CREATE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Rahul"],
    "Age": [22, 24, 23, 25],
    "Department": ["IT", "HR", "Finance", "IT"],
    "Salary": [50000, 65000, 55000, 70000]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. VIEW COLUMN NAMES
# =========================================================

print("========== COLUMN NAMES ==========\n")

print(df.columns)

print("\n")


# # =========================================================
# # 5. SELECT SINGLE COLUMN
# # =========================================================

# print("========== SINGLE COLUMN ==========\n")

# print(df["Name"])

# print("\n")


# # =========================================================
# # 6. SELECT MULTIPLE COLUMNS
# # =========================================================

# print("========== MULTIPLE COLUMNS ==========\n")

# print(df[["Name", "Salary"]])

# print("\n")


# # =========================================================
# # 7. ADD NEW COLUMN
# # =========================================================

# print("========== ADD NEW COLUMN ==========\n")

# df["Bonus"] = [5000, 6500, 5500, 7000]

# print(df)

# print("\n")


# # =========================================================
# # 8. CREATE COLUMN USING CALCULATION
# # =========================================================

# print("========== CALCULATED COLUMN ==========\n")

# df["TotalSalary"] = (
#     df["Salary"] +
#     df["Bonus"]
# )

# print(df)

# print("\n")


# # =========================================================
# # 9. UPDATE EXISTING COLUMN
# # =========================================================

# print("========== UPDATE COLUMN ==========\n")

# df["Age"] = df["Age"] + 1

# print(df)

# print("\n")


# # =========================================================
# # 10. UPDATE COLUMN USING CONDITION
# # =========================================================

# print("========== CONDITIONAL UPDATE ==========\n")

# df.loc[
#     df["Department"] == "IT",
#     "Bonus"
# ] = 10000

# print(df)

# print("\n")


# # =========================================================
# # 11. RENAME SINGLE COLUMN
# # =========================================================

# print("========== RENAME SINGLE COLUMN ==========\n")

# df.rename(
#     columns={"Salary": "MonthlySalary"},
#     inplace=True
# )

# print(df)

# print("\n")


# # =========================================================
# # 12. RENAME MULTIPLE COLUMNS
# # =========================================================

# print("========== RENAME MULTIPLE COLUMNS ==========\n")

# df.rename(
#     columns={
#         "Name": "EmployeeName",
#         "Age": "EmployeeAge"
#     },
#     inplace=True
# )

# print(df)

# print("\n")


# # =========================================================
# # 13. CHANGE COLUMN ORDER
# # =========================================================

# print("========== CHANGE COLUMN ORDER ==========\n")

# df = df[
#     [
#         "EmployeeName",
#         "Department",
#         "MonthlySalary",
#         "Bonus",
#         "TotalSalary",
#         "EmployeeAge"
#     ]
# ]

# print(df)

# print("\n")


# # =========================================================
# # 14. DELETE SINGLE COLUMN
# # =========================================================

# print("========== DELETE SINGLE COLUMN ==========\n")

# temp_df = df.drop(
#     "Bonus",
#     axis=1
# )

# print(temp_df)

# print("\n")


# # =========================================================
# # 15. DELETE MULTIPLE COLUMNS
# # =========================================================

# print("========== DELETE MULTIPLE COLUMNS ==========\n")

# temp_df2 = df.drop(
#     ["Bonus", "TotalSalary"],
#     axis=1
# )

# print(temp_df2)

# print("\n")


# # =========================================================
# # 16. CHECK COLUMN DATA TYPES
# # =========================================================

# print("========== COLUMN DATA TYPES ==========\n")

# print(df.dtypes)

# print("\n")


# # =========================================================
# # 17. CONVERT COLUMN DATA TYPE
# # =========================================================

# print("========== CONVERT DATA TYPE ==========\n")

# df["EmployeeAge"] = df["EmployeeAge"].astype(float)

# print(df.dtypes)

# print("\n")


# # =========================================================
# # 18. CREATE COLUMN USING apply()
# # =========================================================

# print("========== APPLY FUNCTION ==========\n")

# df["Tax"] = df["MonthlySalary"].apply(
#     lambda x: x * 0.10
# )

# print(df)

# print("\n")


# # =========================================================
# # 19. CREATE CATEGORY COLUMN
# # =========================================================

# print("========== CATEGORY COLUMN ==========\n")

# df["SalaryCategory"] = df["MonthlySalary"].apply(
#     lambda x: "High" if x > 60000 else "Low"
# )

# print(df)

# print("\n")


# # =========================================================
# # 20. INSERT COLUMN AT SPECIFIC POSITION
# # =========================================================

# print("========== INSERT COLUMN ==========\n")

# df.insert(
#     1,
#     "City",
#     ["Delhi", "Noida", "Mumbai", "Pune"]
# )

# print(df)

# print("\n")


# # =========================================================
# # 21. CHECK UNIQUE VALUES
# # =========================================================

# print("========== UNIQUE VALUES ==========\n")

# print(df["Department"].unique())

# print("\n")


# # =========================================================
# # 22. VALUE COUNTS
# # =========================================================

# print("========== VALUE COUNTS ==========\n")

# print(df["Department"].value_counts())

# print("\n")


# # =========================================================
# # 23. FILTER SPECIFIC COLUMNS
# # =========================================================

# print("========== FILTER COLUMNS ==========\n")

# filtered_columns = df.filter(
#     items=["EmployeeName", "MonthlySalary"]
# )

# print(filtered_columns)

# print("\n")


# # =========================================================
# # 24. COLUMN STATISTICS
# # =========================================================

# print("========== COLUMN STATISTICS ==========\n")

# print("Maximum Salary:")

# print(df["MonthlySalary"].max())

# print("\nMinimum Salary:")

# print(df["MonthlySalary"].min())

# print("\nAverage Salary:")

# print(df["MonthlySalary"].mean())

# print("\n")


# # =========================================================
# # 25. STRING COLUMN OPERATIONS
# # =========================================================

# print("========== STRING OPERATIONS ==========\n")

# df["EmployeeName"] = (
#     df["EmployeeName"].str.upper()
# )

# print(df)

# print("\n")


# # =========================================================
# # 26. CHECK NULL VALUES
# # =========================================================

# print("========== NULL VALUES ==========\n")

# print(df.isnull().sum())

# print("\n")


# # =========================================================
# # 27. MINI PRACTICE TASK
# # =========================================================

# print("========== MINI PRACTICE TASK ==========\n")

# student_data = {
#     "Student": ["Aman", "Neha", "Rahul"],
#     "Math": [90, 85, 70],
#     "Science": [88, 91, 75]
# }

# students_df = pd.DataFrame(student_data)

# print("ORIGINAL DATA:\n")

# print(students_df)

# print("\n")

# # ADD TOTAL COLUMN
# students_df["Total"] = (
#     students_df["Math"] +
#     students_df["Science"]
# )

# # ADD AVERAGE COLUMN
# students_df["Average"] = (
#     students_df["Total"] / 2
# )

# print("UPDATED DATA:\n")

# print(students_df)

# print("\n")

# print("TOP STUDENT:\n")

# top_student = students_df.sort_values(
#     by="Total",
#     ascending=False
# )

# print(top_student.head(1))

# print("\n")


# # =========================================================
# # 28. REAL-WORLD INDUSTRY LEARNING
# # =========================================================

# print("========== INDUSTRY LEARNING ==========\n")

# """
# Column operations are heavily used in:

# - Data Cleaning
# - Feature Engineering
# - Machine Learning
# - Dashboard Creation

# Examples:
# - Create profit column
# - Create tax column
# - Create age groups
# - Create salary categories

# This process is called:
# Feature Engineering
# """

# print("Column Operations Are Very Important")

# print("\n")


# # =========================================================
# # 29. INTERVIEW QUESTIONS
# # =========================================================

# """
# Q1. How to add a new column?

# Using:
# df["new_column"] = values

# --------------------------------------------------

# Q2. How to rename columns?

# Using:
# df.rename()

# --------------------------------------------------

# Q3. How to delete columns?

# Using:
# df.drop()

# --------------------------------------------------

# Q4. How to change data type?

# Using:
# astype()

# --------------------------------------------------

# Q5. How to create calculated columns?

# Using:
# mathematical operations

# --------------------------------------------------

# Q6. What is Feature Engineering?

# Ans:
# Creating new useful columns/features
# from existing data.

# --------------------------------------------------

# Q7. How to apply functions on columns?

# Using:
# apply()
# """


# # =========================================================
# # 30. END OF FILE
# # =========================================================

# print("========== COLUMN OPERATIONS COMPLETED ==========")