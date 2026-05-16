# =========================================================
# Pandas Filtering & Sorting Tutorial
# Beginner to Advanced
# File: 07_filtering_sorting.py
# =========================================================


# =========================================================
# 1. IMPORT LIBRARIES
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS FILTERING & SORTING?
# =========================================================

"""
Filtering:
Selecting specific rows based on conditions.

Sorting:
Arranging data in ascending or descending order.

Used in:
- Data Analysis
- Machine Learning
- Business Analytics
- Dashboards
"""

print("========== FILTERING & SORTING ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== CREATE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Rahul", "Simran"],
    "Age": [22, 25, 23, 24, 26],
    "City": ["Delhi", "Noida", "Mumbai", "Pune", "Lucknow"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 65000, 55000, 70000, 60000]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. SIMPLE FILTERING
# =========================================================

print("========== SIMPLE FILTERING ==========\n")

high_salary = df[
    df["Salary"] > 60000
]

print(high_salary)

print("\n")


# =========================================================
# 5. FILTER USING LESS THAN
# =========================================================

print("========== LESS THAN FILTER ==========\n")

young_employees = df[
    df["Age"] < 24
]

print(young_employees)

print("\n")


# =========================================================
# 6. FILTER USING EQUAL CONDITION
# =========================================================

print("========== EQUAL CONDITION ==========\n")

it_department = df[
    df["Department"] == "IT"
]

print(it_department)

print("\n")


# =========================================================
# 7. FILTER USING MULTIPLE CONDITIONS
# =========================================================

print("========== MULTIPLE CONDITIONS ==========\n")

result = df[
    (df["Salary"] > 55000) &
    (df["Age"] > 24)
]

print(result)

print("\n")


# =========================================================
# 8. FILTER USING OR CONDITION
# =========================================================

print("========== OR CONDITION ==========\n")

result = df[
    (df["City"] == "Delhi") |
    (df["City"] == "Pune")
]

print(result)

print("\n")


# =========================================================
# 9. FILTER USING isin()
# =========================================================

print("========== isin() ==========\n")

cities = ["Delhi", "Mumbai"]

filtered_df = df[
    df["City"].isin(cities)
]

print(filtered_df)

print("\n")


# =========================================================
# 10. FILTER USING between()
# =========================================================

print("========== between() ==========\n")

salary_range = df[
    df["Salary"].between(55000, 70000)
]

print(salary_range)

print("\n")


# =========================================================
# 11. STRING FILTERING
# =========================================================

print("========== STRING FILTERING ==========\n")

starts_with_m = df[
    df["Name"].str.startswith("M")
]

print(starts_with_m)

print("\n")


# =========================================================
# 12. FILTER USING contains()
# =========================================================

print("========== contains() ==========\n")

contains_o = df[
    df["City"].str.contains("o")
]

print(contains_o)

print("\n")


# =========================================================
# 13. FILTER NULL VALUES
# =========================================================

print("========== NULL VALUE FILTER ==========\n")

data2 = {
    "Name": ["Aman", "Neha", None, "Rahul"],
    "Marks": [90, None, 85, 70]
}

null_df = pd.DataFrame(data2)

print(null_df)

print("\nRows With Null Values:\n")

print(
    null_df[
        null_df.isnull().any(axis=1)
    ]
)

print("\n")


# =========================================================
# 14. QUERY METHOD
# =========================================================

print("========== QUERY METHOD ==========\n")

query_result = df.query(
    "Salary > 55000"
)

print(query_result)

print("\n")


# =========================================================
# 15. SORT ASCENDING
# =========================================================

print("========== SORT ASCENDING ==========\n")

sorted_df = df.sort_values(
    by="Salary"
)

print(sorted_df)

print("\n")


# =========================================================
# 16. SORT DESCENDING
# =========================================================

print("========== SORT DESCENDING ==========\n")

sorted_desc = df.sort_values(
    by="Salary",
    ascending=False
)

print(sorted_desc)

print("\n")


# =========================================================
# 17. SORT MULTIPLE COLUMNS
# =========================================================

print("========== MULTIPLE COLUMN SORT ==========\n")

multi_sort = df.sort_values(
    by=["Department", "Salary"]
)

print(multi_sort)

print("\n")


# =========================================================
# 18. TOP SALARY EMPLOYEES
# =========================================================

print("========== TOP SALARY ==========\n")

top_salary = df.nlargest(
    2,
    "Salary"
)

print(top_salary)

print("\n")


# =========================================================
# 19. LOWEST SALARY EMPLOYEES
# =========================================================

print("========== LOWEST SALARY ==========\n")

lowest_salary = df.nsmallest(
    2,
    "Salary"
)

print(lowest_salary)

print("\n")


# =========================================================
# 20. FILTER SPECIFIC COLUMNS
# =========================================================

print("========== SPECIFIC COLUMNS ==========\n")

selected = df.loc[
    df["Salary"] > 55000,
    ["Name", "Salary"]
]

print(selected)

print("\n")


# =========================================================
# 21. FILTER USING loc[]
# =========================================================

print("========== FILTER USING loc[] ==========\n")

loc_filter = df.loc[
    df["Department"] == "IT"
]

print(loc_filter)

print("\n")


# =========================================================
# 22. FILTER USING iloc[]
# =========================================================

print("========== FILTER USING iloc[] ==========\n")

print(df.iloc[0:3])

print("\n")


# =========================================================
# 23. RESET INDEX AFTER FILTERING
# =========================================================

print("========== RESET INDEX ==========\n")

filtered = df[
    df["Salary"] > 55000
]

print(filtered)

print("\nRESET INDEX:\n")

print(
    filtered.reset_index(drop=True)
)

print("\n")


# =========================================================
# 24. RANDOM SAMPLE
# =========================================================

print("========== RANDOM SAMPLE ==========\n")

print(df.sample(2))

print("\n")


# =========================================================
# 25. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {
    "Student": ["Aman", "Neha", "Rahul", "Simran"],
    "Math": [80, 95, 70, 88],
    "Science": [85, 90, 75, 92],
    "English": [78, 91, 72, 85]
}

students_df = pd.DataFrame(student_data)

print("STUDENT DATA:\n")

print(students_df)

print("\n")

print("Students With Math > 80:\n")

math_filter = students_df[
    students_df["Math"] > 80
]

print(math_filter)

print("\n")

print("Top Student Based On Science:\n")

top_student = students_df.sort_values(
    by="Science",
    ascending=False
)

print(top_student.head(1))

print("\n")


# =========================================================
# 26. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Filtering and sorting are heavily used in:

- Dashboards
- Data Cleaning
- Machine Learning
- SQL-like analysis

Examples:
- Top customers
- Highest sales
- Low-performing students
- IT department employees
- Fraud transactions

Very important in:
- Power BI
- Pandas
- SQL
- Data Analytics
"""

print("Filtering & Sorting Are Industry-Level Skills")

print("\n")


# =========================================================
# 27. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. How to filter rows in Pandas?

Using:
df[df["column"] > value]

--------------------------------------------------

Q2. How to apply multiple conditions?

Using:
&
|

--------------------------------------------------

Q3. How to sort data?

Using:
sort_values()

--------------------------------------------------

Q4. How to get top rows?

Using:
nlargest()

--------------------------------------------------

Q5. Difference between loc[] and iloc[]?

loc[]
- Label based

iloc[]
- Position based

--------------------------------------------------

Q6. How to filter string values?

Using:
str.contains()
str.startswith()

--------------------------------------------------

Q7. Why is filtering important?

Ans:
To analyze specific useful data
from large datasets.
"""


# =========================================================
# 28. END OF FILE
# =========================================================

print("========== FILTERING & SORTING COMPLETED ==========")