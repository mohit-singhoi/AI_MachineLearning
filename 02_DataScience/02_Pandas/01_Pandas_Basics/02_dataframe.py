# =========================================================
# Pandas DataFrame Tutorial
# Beginner to Advanced
# File: 02_dataframe.py
# =========================================================

# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS A DATAFRAME?
# =========================================================

"""
A Pandas DataFrame is:

- A 2-dimensional data structure
- Similar to an Excel table
- Contains rows and columns
- Can store multiple data types

Example:

------------------------------------------------
| Name   | Age | City      | Salary          |
------------------------------------------------
| Mohit  | 22  | Delhi     | 55000           |
| Aman   | 24  | Noida     | 60000           |
------------------------------------------------
"""

print("========== WHAT IS DATAFRAME ==========\n")


# =========================================================
# 3. CREATE SIMPLE DATAFRAME
# =========================================================

print("========== SIMPLE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Simran"],
    "Age": [22, 24, 23, 25],
    "City": ["Delhi", "Noida", "Lucknow", "Mumbai"]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. CHECK DATAFRAME TYPE
# =========================================================

print("========== DATAFRAME TYPE ==========\n")

print(type(df))

print("\n")


# =========================================================
# 5. ACCESS COLUMNS
# =========================================================

print("========== ACCESS SINGLE COLUMN ==========\n")

print(df["Name"])

print("\n")


# =========================================================
# 6. ACCESS MULTIPLE COLUMNS
# =========================================================

print("========== ACCESS MULTIPLE COLUMNS ==========\n")

print(df[["Name", "City"]])

print("\n")


# =========================================================
# 7. ACCESS ROWS USING loc[]
# =========================================================

print("========== ACCESS ROWS USING loc[] ==========\n")

print("First Row:\n")
print(df.loc[0])

print("\n")

print("Multiple Rows:\n")
print(df.loc[[0, 1]])

print("\n")


# =========================================================
# 8. ACCESS ROWS USING iloc[]
# =========================================================

print("========== ACCESS ROWS USING iloc[] ==========\n")

print(df.iloc[2])

print("\n")


# =========================================================
# 9. CUSTOM INDEXES
# =========================================================

print("========== CUSTOM INDEXES ==========\n")

df2 = pd.DataFrame(
    data,
    index=["emp1", "emp2", "emp3", "emp4"]
)

print(df2)

print("\n")


# =========================================================
# 10. ACCESS USING CUSTOM INDEX
# =========================================================

print("========== ACCESS CUSTOM INDEX ==========\n")

print(df2.loc["emp2"])

print("\n")


# =========================================================
# 11. DATAFRAME ATTRIBUTES
# =========================================================

print("========== DATAFRAME ATTRIBUTES ==========\n")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nIndexes:")
print(df.index)

print("\nData Types:")
print(df.dtypes)

print("\nSize:")
print(df.size)

print("\n")


# =========================================================
# 12. HEAD() AND TAIL()
# =========================================================

print("========== HEAD & TAIL ==========\n")

print("First 2 Rows:\n")
print(df.head(2))

print("\nLast 2 Rows:\n")
print(df.tail(2))

print("\n")


# =========================================================
# 13. INFO()
# =========================================================

print("========== INFO ==========\n")

print(df.info())

print("\n")


# =========================================================
# 14. DESCRIBE()
# =========================================================

print("========== DESCRIBE ==========\n")

print(df.describe())

print("\n")


# =========================================================
# 15. ADD NEW COLUMN
# =========================================================

print("========== ADD NEW COLUMN ==========\n")

df["Salary"] = [50000, 60000, 55000, 70000]

print(df)

print("\n")



# =========================================================
# 16. UPDATE COLUMN
# =========================================================

print("========== UPDATE COLUMN ==========\n")

df["Age"] = df["Age"] + 1

print(df)

print("\n")


# =========================================================
# 17. DELETE COLUMN
# =========================================================

print("========== DELETE COLUMN ==========\n")

df.drop("City", axis=1, inplace=True)

print(df)

print("\n")



# =========================================================
# 18. RENAME COLUMNS
# =========================================================

print("========== RENAME COLUMNS ==========\n")

df.rename(columns={"Salary": "MonthlySalary"}, inplace=True)

print(df)

print("\n")


# =========================================================
# 19. FILTERING DATA
# =========================================================

print("========== FILTERING DATA ==========\n")

result = df[df["MonthlySalary"] > 55000]

print(result)

print("\n")


# =========================================================
# 20. SORTING DATA
# =========================================================

print("========== SORTING ==========\n")

sorted_df = df.sort_values(by="MonthlySalary")

print(sorted_df)

print("\n")


# =========================================================
# 21. SORT DESCENDING
# =========================================================

print("========== SORT DESCENDING ==========\n")

sorted_desc = df.sort_values(
    by="MonthlySalary",
    ascending=False
)

print(sorted_desc)

print("\n")


# =========================================================
# 22. NULL VALUES
# =========================================================

print("========== NULL VALUES ==========\n")

data2 = {
    "Name": ["A", "B", "C", None],
    "Marks": [90, None, 85, 70]
}

null_df = pd.DataFrame(data2)

print(null_df)

print("\nCheck Null Values:\n")
print(null_df.isnull())

print("\nCount Null Values:\n")
print(null_df.isnull().sum())

print("\n")


# =========================================================
# 23. FILL NULL VALUES
# =========================================================

print("========== FILL NULL VALUES ==========\n")

filled_df = null_df.fillna(0)

print(filled_df)

print("\n")


# =========================================================
# 24. DROP NULL VALUES
# =========================================================

print("========== DROP NULL VALUES ==========\n")

dropped_df = null_df.dropna()

print(dropped_df)

print("\n")


# =========================================================
# 25. VALUE COUNTS
# =========================================================

print("========== VALUE COUNTS ==========\n")

print(df["Age"].value_counts())

print("\n")


# =========================================================
# 26. UNIQUE VALUES
# =========================================================

print("========== UNIQUE VALUES ==========\n")

print(df["Age"].unique())

print("\n")


# =========================================================
# 27. APPLY FUNCTION
# =========================================================

print("========== APPLY FUNCTION ==========\n")

df["Bonus"] = df["MonthlySalary"].apply(
    lambda x: x * 0.10
)

print(df)

print("\n")


# =========================================================
# 28. BASIC STATISTICS
# =========================================================

print("========== BASIC STATISTICS ==========\n")

print("Average Salary:")
print(df["MonthlySalary"].mean())

print("\nMaximum Salary:")
print(df["MonthlySalary"].max())

print("\nMinimum Salary:")
print(df["MonthlySalary"].min())

print("\n")


# =========================================================
# 29. MINI PRACTICE PROJECT
# =========================================================

print("========== MINI PRACTICE PROJECT ==========\n")

student_data = {
    "Student": ["Rahul", "Mohit", "Neha", "Aman"],
    "Math": [90, 85, 95, 70],
    "Science": [88, 91, 89, 75],
    "English": [92, 80, 87, 78]
}

students_df = pd.DataFrame(student_data)

print(students_df)

print("\n")

students_df["Total"] = (
    students_df["Math"] +
    students_df["Science"] +
    students_df["English"]
)

students_df["Average"] = students_df["Total"] / 3

print(students_df)

print("\nTop Student:\n")

top_student = students_df.sort_values(
    by="Total",
    ascending=False
)

print(top_student.head(1))

print("\n")


# =========================================================
# 30. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What is a DataFrame?

Ans:
A two-dimensional labeled data structure
with rows and columns.

--------------------------------------------------

Q2. Difference between Series and DataFrame?

Series:
- One-dimensional

DataFrame:
- Two-dimensional

--------------------------------------------------

Q3. How to access rows?

Using:
- loc[]
- iloc[]

--------------------------------------------------

Q4. How to check null values?

Using:
df.isnull()

--------------------------------------------------

Q5. How to remove columns?

Using:
df.drop()

--------------------------------------------------

Q6. How to rename columns?

Using:
df.rename()

--------------------------------------------------

Q7. How to filter rows?

Using:
df[df["column"] > value]
"""

# =========================================================
# 31. END OF FILE
# =========================================================

print("========== DATAFRAME TUTORIAL COMPLETED ==========")