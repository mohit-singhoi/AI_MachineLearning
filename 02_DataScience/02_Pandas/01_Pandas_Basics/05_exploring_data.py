# =========================================================
# Pandas Exploring Data Tutorial
# Beginner to Advanced
# File: 05_exploring_data.py
# =========================================================

# =========================================================
# 1. IMPORT LIBRARIES
# =========================================================

from pathlib import Path
import pandas as pd


# =========================================================
# 2. WHAT IS DATA EXPLORATION?
# =========================================================

"""
Data Exploration means:

- Understanding dataset structure
- Checking rows & columns
- Finding missing values
- Understanding data types
- Finding patterns in data

Used in:
    • Data Science
    • Machine Learning
    • Business Analytics
    • Deep Learning
"""

print("========== DATA EXPLORATION ==========\n")


# =========================================================
# 3. BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# 4. DATASET PATH
# =========================================================

csv_path = BASE_DIR.parent / "datasets" / "employees.csv"


# =========================================================
# 5. READ CSV FILE
# =========================================================

print("========== READ DATASET ==========\n")

df = pd.read_csv(csv_path)

print(df)

print("\n")


# =========================================================
# 6. HEAD()
# =========================================================

print("========== HEAD() ==========\n")

print(df.head())

print("\n")


# =========================================================
# 7. TAIL()
# =========================================================

print("========== TAIL() ==========\n")

print(df.tail())

print("\n")


# =========================================================
# 8. SHAPE OF DATASET
# =========================================================

print("========== SHAPE ==========\n")

print(df.shape)

print("\n")


# =========================================================
# 9. TOTAL ROWS & COLUMNS
# =========================================================

print("========== ROWS & COLUMNS ==========\n")

print("Total Rows:", df.shape[0])

print("Total Columns:", df.shape[1])

print("\n")


# =========================================================
# 10. COLUMN NAMES
# =========================================================

print("========== COLUMN NAMES ==========\n")

print(df.columns)

print("\n")


# =========================================================
# 11. DATA TYPES
# =========================================================

print("========== DATA TYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 12. DATASET INFORMATION
# =========================================================

print("========== INFO() ==========\n")

print(df.info())

print("\n")


# =========================================================
# 13. STATISTICAL SUMMARY
# =========================================================

print("========== DESCRIBE() ==========\n")

print(df.describe())

print("\n")


# =========================================================
# 14. CHECK NULL VALUES
# =========================================================

print("========== NULL VALUES ==========\n")

print(df.isnull())

print("\n")


# =========================================================
# 15. COUNT NULL VALUES
# =========================================================

print("========== NULL VALUE COUNT ==========\n")

print(df.isnull().sum())

print("\n")


# =========================================================
# 16. CHECK DUPLICATE ROWS
# =========================================================

print("========== DUPLICATE ROWS ==========\n")

print(df.duplicated())

print("\n")


# =========================================================
# 17. COUNT DUPLICATES
# =========================================================

print("========== DUPLICATE COUNT ==========\n")

print(df.duplicated().sum())

print("\n")


# =========================================================
# 18. UNIQUE VALUES
# =========================================================

print("========== UNIQUE DEPARTMENTS ==========\n")

print(df["Department"].unique())

print("\n")


# =========================================================
# 19. VALUE COUNTS
# =========================================================

print("========== VALUE COUNTS ==========\n")

print(df["Department"].value_counts())

print("\n")


# =========================================================
# 20. MAXIMUM SALARY
# =========================================================

print("========== MAXIMUM SALARY ==========\n")

print(df["Salary"].max())

print("\n")


# =========================================================
# 21. MINIMUM SALARY
# =========================================================

print("========== MINIMUM SALARY ==========\n")

print(df["Salary"].min())

print("\n")


# =========================================================
# 22. AVERAGE SALARY
# =========================================================

print("========== AVERAGE SALARY ==========\n")

print(df["Salary"].mean())

print("\n")


# =========================================================
# 23. MEDIAN SALARY
# =========================================================

print("========== MEDIAN SALARY ==========\n")

print(df["Salary"].median())

print("\n")


# =========================================================
# 24. MODE OF DEPARTMENT
# =========================================================

print("========== MODE OF DEPARTMENT ==========\n")

print(df["Department"].mode())

print("\n")


# =========================================================
# 25. STANDARD DEVIATION
# =========================================================

print("========== STANDARD DEVIATION ==========\n")

print(df["Salary"].std())

print("\n")


# =========================================================
# 26. SORT DATA
# =========================================================

print("========== SORT DATA ==========\n")

sorted_df = df.sort_values(
    by="Salary",
    ascending=False
)

print(sorted_df)

print("\n")


# =========================================================
# 27. FILTER HIGH SALARY EMPLOYEES
# =========================================================

print("========== HIGH SALARY EMPLOYEES ==========\n")

high_salary = df[df["Salary"] > 60000]

print(high_salary)

print("\n")


# =========================================================
# 28. SELECT SPECIFIC COLUMNS
# =========================================================

print("========== SELECT SPECIFIC COLUMNS ==========\n")

selected_columns = df[
    ["EmployeeName", "Salary"]
]

print(selected_columns)

print("\n")


# =========================================================
# 29. RANDOM SAMPLE
# =========================================================

print("========== RANDOM SAMPLE ==========\n")

print(df.sample(3))

print("\n")


# =========================================================
# 30. CORRELATION
# =========================================================

print("========== CORRELATION ==========\n")

numeric_df = df.select_dtypes(include="number")

print(numeric_df.corr())

print("\n")


# =========================================================
# 31. MEMORY USAGE
# =========================================================

print("========== MEMORY USAGE ==========\n")

print(df.memory_usage())

print("\n")


# =========================================================
# 32. LARGEST SALARY ROW
# =========================================================

print("========== HIGHEST SALARY EMPLOYEE ==========\n")

highest_salary = df.nlargest(1, "Salary")

print(highest_salary)

print("\n")


# =========================================================
# 33. LOWEST SALARY ROW
# =========================================================

print("========== LOWEST SALARY EMPLOYEE ==========\n")

lowest_salary = df.nsmallest(1, "Salary")

print(lowest_salary)

print("\n")


# =========================================================
# 34. GROUP BY DEPARTMENT
# =========================================================

print("========== GROUP BY DEPARTMENT ==========\n")

grouped = df.groupby("Department")["Salary"].mean()

print(grouped)

print("\n")


# =========================================================
# 35. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {
    "Student": ["Aman", "Neha", "Rahul", "Simran"],
    "Math": [80, 95, 70, 88],
    "Science": [85, 90, 75, 92],
    "English": [78, 91, 72, 85]
}

students_df = pd.DataFrame(student_data)

print(students_df)

print("\nTop Math Student:\n")

top_math = students_df.nlargest(1, "Math")

print(top_math)

print("\nAverage Science Marks:\n")

print(students_df["Science"].mean())

print("\n")


# =========================================================
# 36. MINI PROJECT TASK
# =========================================================

print("========== MINI PROJECT TASK ==========\n")

sales_path = BASE_DIR.parent / "datasets" / "sales_data.csv"

sales_df = pd.read_csv(sales_path)

print(sales_df.head())

print("\nTotal Revenue:\n")

sales_df["Revenue"] = (
    sales_df["Quantity"] *
    sales_df["Price"]
)

print(sales_df)

print("\nHighest Revenue Product:\n")

highest_revenue = sales_df.nlargest(1, "Revenue")

print(highest_revenue)

print("\n")


# =========================================================
# 37. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What is Data Exploration?

Understanding and analyzing dataset structure.

--------------------------------------------------

Q2. How to check dataset shape?

Using:
df.shape

--------------------------------------------------

Q3. How to get column names?

Using:
df.columns

--------------------------------------------------

Q4. How to check data types?

Using:
df.dtypes

--------------------------------------------------

Q5. How to check dataset information?

Using:
df.info()

--------------------------------------------------

Q6. How to check null values?

Using:
df.isnull()

--------------------------------------------------

Q7. How to count missing values?

Using:
df.isnull().sum()

--------------------------------------------------

Q8. How to check duplicate rows?

Using:
df.duplicated()

--------------------------------------------------

Q9. How to get statistical summary?

Using:
df.describe()

--------------------------------------------------

Q10. Why is EDA important?

Because it helps understand data before
Machine Learning and Data Analysis.
"""


# =========================================================
# 38. END OF FILE
# =========================================================

print("========== EXPLORING DATA COMPLETED ==========")