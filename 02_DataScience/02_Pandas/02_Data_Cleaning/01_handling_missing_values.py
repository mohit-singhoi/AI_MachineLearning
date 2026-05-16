# =========================================================
# Pandas Missing Values Handling Tutorial
# Beginner to Advanced
# File: 01_missing_values.py
# Folder: 02_Data_Cleaning
# =========================================================


# =========================================================
# 1. IMPORT LIBRARIES
# =========================================================

import pandas as pd
import numpy as np


# =========================================================
# 2. WHAT ARE MISSING VALUES?
# =========================================================

"""
Missing Values means:

- Data is not available
- Empty cells
- Null values

Represented as:
- NaN
- None

Very common in:
- Real-world datasets
- Machine Learning
- Data Analysis

Examples:
- Missing salary
- Missing age
- Missing department
"""

print("========== MISSING VALUES ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", None, "Simran"],
    "Age": [22, 25, np.nan, 24, 26],
    "Department": ["IT", None, "Finance", "HR", "IT"],
    "Salary": [50000, 65000, 55000, np.nan, 70000]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. CHECK NULL VALUES
# =========================================================

print("========== CHECK NULL VALUES ==========\n")

print(df.isnull())

print("\n")


# =========================================================
# 5. COUNT NULL VALUES
# =========================================================

print("========== COUNT NULL VALUES ==========\n")

print(df.isnull().sum())

print("\n")


# =========================================================
# 6. CHECK NON-NULL VALUES
# =========================================================

print("========== NON-NULL VALUES ==========\n")

print(df.notnull())

print("\n")


# =========================================================
# 7. TOTAL MISSING VALUES
# =========================================================

print("========== TOTAL MISSING VALUES ==========\n")

print(df.isnull().sum().sum())

print("\n")


# =========================================================
# 8. CHECK ROWS WITH NULL VALUES
# =========================================================

print("========== ROWS WITH NULL VALUES ==========\n")

null_rows = df[
    df.isnull().any(axis=1)
]

print(null_rows)

print("\n")


# =========================================================
# 9. DROP ROWS WITH NULL VALUES
# =========================================================

print("========== DROP NULL ROWS ==========\n")

dropped_rows = df.dropna()

print(dropped_rows)

print("\n")


# =========================================================
# 10. DROP COLUMNS WITH NULL VALUES
# =========================================================

print("========== DROP NULL COLUMNS ==========\n")

dropped_columns = df.dropna(axis=1)

print(dropped_columns)

print("\n")


# =========================================================
# 11. FILL NULL VALUES WITH 0
# =========================================================

print("========== FILL NULL WITH 0 ==========\n")

filled_zero = df.fillna(0)

print(filled_zero)

print("\n")


# =========================================================
# 12. FILL NULL VALUES WITH CUSTOM VALUE
# =========================================================

print("========== CUSTOM FILL ==========\n")

filled_custom = df.fillna(
    {
        "Name": "Unknown",
        "Department": "Not Assigned",
        "Age": 0,
        "Salary": 0
    }
)

print(filled_custom)

print("\n")


# =========================================================
# 13. FILL USING MEAN
# =========================================================

print("========== FILL USING MEAN ==========\n")

mean_age = df["Age"].mean()

df["Age"] = df["Age"].fillna(mean_age)

print(df)

print("\n")


# =========================================================
# 14. FILL USING MEDIAN
# =========================================================

print("========== FILL USING MEDIAN ==========\n")

median_salary = df["Salary"].median()

df["Salary"] = df["Salary"].fillna(
    median_salary
)

print(df)

print("\n")


# =========================================================
# 15. FILL USING MODE
# =========================================================

print("========== FILL USING MODE ==========\n")

mode_department = (
    df["Department"].mode()[0]
)

df["Department"] = df["Department"].fillna(
    mode_department
)

print(df)

print("\n")


# =========================================================
# 16. FORWARD FILL
# =========================================================

print("========== FORWARD FILL ==========\n")

forward_fill_df = df.ffill()

print(forward_fill_df)

print("\n")


# =========================================================
# 17. BACKWARD FILL
# =========================================================

print("========== BACKWARD FILL ==========\n")

backward_fill_df = df.bfill()

print(backward_fill_df)

print("\n")


# =========================================================
# 18. CHECK DATA TYPES
# =========================================================

print("========== DATA TYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 19. REPLACE NULL VALUES
# =========================================================

print("========== REPLACE NULL VALUES ==========\n")

replace_df = pd.DataFrame({
    "Marks": [90, np.nan, 85, np.nan]
})

print("ORIGINAL:\n")

print(replace_df)

print("\n")

replace_df.replace(
    np.nan,
    0,
    inplace=True
)

print("UPDATED:\n")

print(replace_df)

print("\n")


# =========================================================
# 20. PERCENTAGE OF MISSING VALUES
# =========================================================

print("========== MISSING VALUE PERCENTAGE ==========\n")

missing_percentage = (
    df.isnull().sum() / len(df)
) * 100

print(missing_percentage)

print("\n")


# =========================================================
# 21. REMOVE ROWS WITH SPECIFIC NULLS
# =========================================================

print("========== DROP SPECIFIC NULLS ==========\n")

specific_drop = df.dropna(
    subset=["Name"]
)

print(specific_drop)

print("\n")


# =========================================================
# 22. THRESHOLD NULL HANDLING
# =========================================================

print("========== THRESHOLD HANDLING ==========\n")

threshold_df = df.dropna(
    thresh=3
)

print(threshold_df)

print("\n")


# =========================================================
# 23. INTERPOLATION
# =========================================================

print("========== INTERPOLATION ==========\n")

data2 = {
    "Sales": [1000, np.nan, 3000, np.nan, 5000]
}

sales_df = pd.DataFrame(data2)

print("ORIGINAL DATA:\n")

print(sales_df)

print("\n")

sales_df["Sales"] = (
    sales_df["Sales"].interpolate()
)

print("INTERPOLATED DATA:\n")

print(sales_df)

print("\n")


# =========================================================
# 24. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {
    "Student": ["Aman", "Neha", None, "Simran"],
    "Math": [80, np.nan, 70, 88],
    "Science": [85, 90, np.nan, 92]
}

students_df = pd.DataFrame(student_data)

print("ORIGINAL DATA:\n")

print(students_df)

print("\n")

print("NULL VALUE COUNT:\n")

print(students_df.isnull().sum())

print("\n")

# FILL NULL VALUES
students_df["Math"] = (
    students_df["Math"].fillna(
        students_df["Math"].mean()
    )
)

students_df["Science"] = (
    students_df["Science"].fillna(
        students_df["Science"].mean()
    )
)

students_df["Student"] = (
    students_df["Student"].fillna(
        "Unknown"
    )
)

print("UPDATED DATA:\n")

print(students_df)

print("\n")


# =========================================================
# 25. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Handling Missing Values is one of the
most important tasks in Data Cleaning.

In real-world projects:
- Datasets are rarely clean
- Missing data is extremely common

Common techniques:
- Drop rows
- Fill with mean
- Fill with median
- Fill with mode
- Interpolation

Used heavily in:
- Machine Learning
- Data Science
- AI Projects
"""

print("Missing Value Handling Is Industry Critical")

print("\n")


# =========================================================
# 26. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What are missing values?

Ans:
Values that are empty or unavailable.

--------------------------------------------------

Q2. How to check missing values?

Using:
isnull()

--------------------------------------------------

Q3. How to count null values?

Using:
isnull().sum()

--------------------------------------------------

Q4. How to remove null values?

Using:
dropna()

--------------------------------------------------

Q5. How to fill null values?

Using:
fillna()

--------------------------------------------------

Q6. Difference between mean and median filling?

Mean:
Average value

Median:
Middle value

--------------------------------------------------

Q7. What is forward fill?

Ans:
Copies previous value into null value.

--------------------------------------------------

Q8. Why is missing value handling important?

Ans:
Because ML models cannot properly
work with missing data.
"""


# =========================================================
# 27. END OF FILE
# =========================================================

print("========== MISSING VALUE HANDLING COMPLETED ==========")