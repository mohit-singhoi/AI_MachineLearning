# =========================================================
# Pandas Indexing & Selection Tutorial
# Beginner to Advanced
# File: 03_indexing_selection.py
# =========================================================

# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Rahul", "Simran"],
    "Age": [22, 25, 23, 24, 26],
    "City": ["Delhi", "Noida", "Mumbai", "Pune", "Lucknow"],
    "Salary": [50000, 65000, 55000, 70000, 60000]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 3. SELECT SINGLE COLUMN
# =========================================================

print("========== SELECT SINGLE COLUMN ==========\n")

print(df["Name"])

print("\n")


# =========================================================
# 4. SELECT MULTIPLE COLUMNS
# =========================================================

print("========== SELECT MULTIPLE COLUMNS ==========\n")

print(df[["Name", "Salary"]])

print("\n")


# =========================================================
# 5. SELECT ROW USING loc[]
# =========================================================

print("========== SELECT ROW USING loc[] ==========\n")

print(df.loc[0])

print("\n")


# =========================================================
# 6. SELECT MULTIPLE ROWS USING loc[]
# =========================================================

print("========== MULTIPLE ROWS USING loc[] ==========\n")

print(df.loc[[0, 2, 4]])

print("\n")


# =========================================================
# 7. SELECT ROWS & COLUMNS USING loc[]
# =========================================================

print("========== ROWS & COLUMNS USING loc[] ==========\n")

print(df.loc[0:2, ["Name", "Salary"]])

print("\n")


# =========================================================
# 8. SELECT USING iloc[]
# =========================================================

print("========== SELECT USING iloc[] ==========\n")

print(df.iloc[0])

print("\n")


# =========================================================
# 9. MULTIPLE ROWS USING iloc[]
# =========================================================

print("========== MULTIPLE ROWS USING iloc[] ==========\n")

print(df.iloc[[1, 3]])

print("\n")


# =========================================================
# 10. ROWS & COLUMNS USING iloc[]
# =========================================================

print("========== ROWS & COLUMNS USING iloc[] ==========\n")

print(df.iloc[0:4, 0:2])

print("\n")


# =========================================================
# 11. BOOLEAN FILTERING
# =========================================================

print("========== BOOLEAN FILTERING ==========\n")

result = df[df["Salary"] > 55000]

print(result)

print("\n")


# =========================================================
# 12. MULTIPLE CONDITIONS
# =========================================================

print("========== MULTIPLE CONDITIONS ==========\n")

result = df[
    (df["Salary"] > 55000) &
    (df["Age"] > 24)
]

print(result)

print("\n")


# =========================================================
# 13. OR CONDITION
# =========================================================

print("========== OR CONDITION ==========\n")

result = df[
    (df["City"] == "Delhi") |
    (df["City"] == "Pune")
]

print(result)

print("\n")


# =========================================================
# 14. FILTER USING isin()
# =========================================================

print("========== FILTER USING isin() ==========\n")

cities = ["Delhi", "Mumbai"]

result = df[df["City"].isin(cities)]

print(result)

print("\n")


# =========================================================
# 15. FILTER USING BETWEEN
# =========================================================

print("========== FILTER USING BETWEEN ==========\n")

result = df[df["Salary"].between(55000, 70000)]

print(result)

print("\n")


# =========================================================
# 16. STRING FILTERING
# =========================================================

print("========== STRING FILTERING ==========\n")

result = df[df["Name"].str.startswith("M")]

print(result)

print("\n")


# =========================================================
# 17. CONTAINS()
# =========================================================

print("========== CONTAINS ==========\n")

result = df[df["City"].str.contains("o")]

print(result)

print("\n")


# =========================================================
# 18. CUSTOM INDEXES
# =========================================================

print("========== CUSTOM INDEXES ==========\n")

df2 = pd.DataFrame(
    data,
    index=["emp1", "emp2", "emp3", "emp4", "emp5"]
)

print(df2)

print("\n")


# =========================================================
# 19. SELECT USING CUSTOM INDEX
# =========================================================

print("========== CUSTOM INDEX SELECTION ==========\n")

print(df2.loc["emp3"])

print("\n")


# =========================================================
# 20. SLICING ROWS
# =========================================================

print("========== ROW SLICING ==========\n")

print(df[1:4])

print("\n")


# =========================================================
# 21. SELECT SPECIFIC CELL
# =========================================================

print("========== SPECIFIC CELL ==========\n")

print(df.loc[0, "Name"])

print("\n")

print(df.iloc[1, 3])

print("\n")


# =========================================================
# 22. CONDITIONAL COLUMN SELECTION
# =========================================================

print("========== CONDITIONAL COLUMN SELECTION ==========\n")

result = df.loc[df["Salary"] > 55000, ["Name", "Salary"]]

print(result)

print("\n")



# =========================================================
# 23. SORTING DATA
# =========================================================

print("========== SORTING ==========\n")

sorted_df = df.sort_values(by="Salary")

print(sorted_df)

print("\n")


# =========================================================
# 24. SORT DESCENDING
# =========================================================

print("========== SORT DESCENDING ==========\n")

sorted_desc = df.sort_values(
    by="Salary",
    ascending=False
)

print(sorted_desc)

print("\n")


# =========================================================
# 25. RESET INDEX
# =========================================================

print("========== RESET INDEX ==========\n")

filtered = df[df["Salary"] > 55000]

print(filtered)

print("\nReset Index:\n")

print(filtered.reset_index(drop=True))

print("\n")


# =========================================================
# 26. SET INDEX
# =========================================================

print("========== SET INDEX ==========\n")

new_df = df.set_index("Name")

print(new_df)

print("\n")


# =========================================================
# 27. SELECT USING QUERY()
# =========================================================

print("========== QUERY METHOD ==========\n")

result = df.query("Salary > 55000")

print(result)

print("\n")


# =========================================================
# 28. SELECT TOP ROWS
# =========================================================

print("========== TOP ROWS ==========\n")

top_salary = df.nlargest(2, "Salary")

print(top_salary)

print("\n")


# =========================================================
# 29. SELECT LOWEST ROWS
# =========================================================

print("========== LOWEST ROWS ==========\n")

lowest_salary = df.nsmallest(2, "Salary")

print(lowest_salary)

print("\n")


# =========================================================
# 30. MINI PRACTICE TASK
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

print("\nStudents With Math > 80:\n")

print(students_df[students_df["Math"] > 80])

print("\nTop Student Based On Science:\n")

top_student = students_df.nlargest(1, "Science")

print(top_student)

print("\n")


# =========================================================
# 31. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. Difference between loc[] and iloc[]?

loc[]
- Label based selection

iloc[]
- Index position based selection

--------------------------------------------------

Q2. How to filter rows in Pandas?

Using:
df[df["column"] > value]

--------------------------------------------------

Q3. How to apply multiple conditions?

Using:
&
|
operators

--------------------------------------------------

Q4. How to select specific rows and columns?

Using:
loc[] or iloc[]

--------------------------------------------------

Q5. How to reset index?

Using:
reset_index()

--------------------------------------------------

Q6. How to set a custom index?

Using:
set_index()

--------------------------------------------------

Q7. What is boolean indexing?

Selecting rows based on conditions.
"""

# =========================================================
# 32. END OF FILE
# =========================================================

print("========== INDEXING & SELECTION COMPLETED ==========")