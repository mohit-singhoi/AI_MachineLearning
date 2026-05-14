# =========================================================
# Pandas Series Tutorial
# Beginner to Advanced
# File: 01_series.py
# =========================================================

# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS A SERIES?
# =========================================================

"""
A Pandas Series is:

- One-dimensional labeled array
- Similar to a single column in Excel
- Can store integers, strings, floats, etc.
- Each value has an index

Example:

Index    Value
0        10
1        20
2        30
"""

print("========== WHAT IS SERIES ==========\n")


# =========================================================
# 3. CREATE A SIMPLE SERIES
# =========================================================

print("========== SIMPLE SERIES ==========\n")

s = pd.Series([10, 20, 30, 40, 50])

print(s)

print("\n")


# =========================================================
# 4. ACCESSING ELEMENTS
# =========================================================

print("========== ACCESSING ELEMENTS ==========\n")

print("First Element :", s[0])
print("Second Element:", s[1])
print("Last Element  :", s[4])

print("\n")


# =========================================================
# 5. SERIES WITH CUSTOM LABELS
# =========================================================

print("========== CUSTOM LABELS ==========\n")

students = pd.Series(
    [85, 90, 78, 92],
    index=["Rahul", "Mohit", "Aman", "Neha"]
)

print(students)

print("\n")


# =========================================================
# 6. ACCESS USING LABELS
# =========================================================

print("========== ACCESS USING LABELS ==========\n")

print("Mohit's Marks:", students["Mohit"])
print("Neha's Marks :", students["Neha"])

print("\n")


# =========================================================
# 7. SERIES FROM DICTIONARY
# =========================================================

print("========== SERIES FROM DICTIONARY ==========\n")

data = {
    "Math": 95,
    "Science": 88,
    "English": 91
}

subjects = pd.Series(data)

print(subjects)

print("\n")


# =========================================================
# 8. SELECT SPECIFIC ITEMS
# =========================================================

print("========== SELECT SPECIFIC ITEMS ==========\n")

selected = pd.Series(data, index=["Math", "English"])

print(selected)

print("\n")


# =========================================================
# 9. SERIES ATTRIBUTES
# =========================================================

print("========== SERIES ATTRIBUTES ==========\n")

print("Values:")
print(s.values)

print("\nIndexes:")
print(s.index)

print("\nDatatype:")
print(s.dtype)

print("\nShape:")
print(s.shape)

print("\nSize:")
print(s.size)

print("\n")


# =========================================================
# 10. MATHEMATICAL OPERATIONS
# =========================================================

print("========== MATHEMATICAL OPERATIONS ==========\n")

numbers = pd.Series([1, 2, 3, 4, 5])

print("Original Series:")
print(numbers)

print("\nAddition:")
print(numbers + 10)

print("\nMultiplication:")
print(numbers * 2)

print("\nSquare:")
print(numbers ** 2)

print("\n")


# =========================================================
# 11. FILTERING DATA
# =========================================================

print("========== FILTERING DATA ==========\n")

marks = pd.Series([45, 67, 89, 90, 34, 76])

print("Original Marks:")
print(marks)

print("\nMarks Greater Than 60:")
print(marks[marks > 60])

print("\n")


# =========================================================
# 12. CHECKING NULL VALUES
# =========================================================

print("========== NULL VALUES ==========\n")

data_with_null = pd.Series([10, 20, None, 40, None])

print(data_with_null)

print("\nCheck Null Values:")
print(data_with_null.isnull())

print("\nTotal Null Values:")
print(data_with_null.isnull().sum())

print("\n")


# =========================================================
# 13. FILL NULL VALUES
# =========================================================

print("========== FILL NULL VALUES ==========\n")

filled = data_with_null.fillna(0)

print(filled)

print("\n")


# =========================================================
# 14. BASIC STATISTICS
# =========================================================

print("========== BASIC STATISTICS ==========\n")

stats = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(stats)

print("\nSum:", stats.sum())
print("Mean:", stats.mean())
print("Maximum:", stats.max())
print("Minimum:", stats.min())
print("Standard Deviation:", stats.std())

print("\n")


# =========================================================
# 15. SORTING
# =========================================================

print("========== SORTING ==========\n")

unsorted = pd.Series([50, 10, 30, 20, 40])

print("Original:")
print(unsorted)

print("\nSorted Ascending:")
print(unsorted.sort_values())

print("\nSorted Descending:")
print(unsorted.sort_values(ascending=False))

print("\n")


# =========================================================
# 16. VALUE COUNTS
# =========================================================

print("========== VALUE COUNTS ==========\n")

values = pd.Series([1, 2, 2, 3, 3, 3, 4])

print(values.value_counts())

print("\n")


# =========================================================
# 17. APPLY FUNCTION
# =========================================================

print("========== APPLY FUNCTION ==========\n")

nums = pd.Series([1, 2, 3, 4, 5])

result = nums.apply(lambda x: x * 10)

print(result)

print("\n")


# =========================================================
# 18. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

employee_salary = pd.Series(
    [25000, 30000, 28000, 35000],
    index=["Aman", "Rohit", "Neha", "Simran"]
)

print(employee_salary)

print("\nAverage Salary:")
print(employee_salary.mean())

print("\nHighest Salary:")
print(employee_salary.max())

print("\nEmployees with Salary > 28000:")
print(employee_salary[employee_salary > 28000])

print("\n")


# =========================================================
# 19. IMPORTANT INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What is a Pandas Series?

Ans:
A one-dimensional labeled array capable of holding
different data types.

--------------------------------------------------

Q2. Difference between NumPy Array and Pandas Series?

NumPy Array:
- No labels/indexes

Pandas Series:
- Has labels/indexes

--------------------------------------------------

Q3. How to create a Series?

pd.Series(data)

--------------------------------------------------

Q4. How to access Series elements?

Using:
- Index Position
- Labels

--------------------------------------------------

Q5. How to handle missing values?

Using:
- fillna()
- dropna()
"""

# =========================================================
# 20. END OF FILE
# =========================================================

print("========== SERIES TUTORIAL COMPLETED ==========")

