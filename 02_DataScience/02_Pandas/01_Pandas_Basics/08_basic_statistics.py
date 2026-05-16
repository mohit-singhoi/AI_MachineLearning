# =========================================================
# Pandas Basic Statistics Tutorial
# Beginner to Advanced
# File: 08_basic_statistics.py
# =========================================================


# =========================================================
# 1. IMPORT LIBRARIES
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS STATISTICS IN PANDAS?
# =========================================================

"""
Statistics helps us understand data.

Used for:
- Data Analysis
- Machine Learning
- Business Intelligence
- Data Science

Common Statistics:
- Mean
- Median
- Mode
- Maximum
- Minimum
- Standard Deviation
"""

print("========== BASIC STATISTICS ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== CREATE DATAFRAME ==========\n")

data = {
    "Name": ["Mohit", "Aman", "Neha", "Rahul", "Simran"],
    "Age": [22, 25, 23, 24, 26],
    "Salary": [50000, 65000, 55000, 70000, 60000],
    "Experience": [1, 3, 2, 4, 5]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. DESCRIBE DATA
# =========================================================

print("========== DESCRIBE() ==========\n")

print(df.describe())

print("\n")


# =========================================================
# 5. MEAN
# =========================================================

print("========== MEAN ==========\n")

print("Average Salary:")

print(df["Salary"].mean())

print("\n")


# =========================================================
# 6. MEDIAN
# =========================================================

print("========== MEDIAN ==========\n")

print("Median Salary:")

print(df["Salary"].median())

print("\n")


# =========================================================
# 7. MODE
# =========================================================

print("========== MODE ==========\n")

print("Mode Of Experience:")

print(df["Experience"].mode())

print("\n")


# =========================================================
# 8. MAXIMUM VALUE
# =========================================================

print("========== MAXIMUM ==========\n")

print("Highest Salary:")

print(df["Salary"].max())

print("\n")


# =========================================================
# 9. MINIMUM VALUE
# =========================================================

print("========== MINIMUM ==========\n")

print("Lowest Salary:")

print(df["Salary"].min())

print("\n")


# =========================================================
# 10. SUM
# =========================================================

print("========== SUM ==========\n")

print("Total Salary:")

print(df["Salary"].sum())

print("\n")


# =========================================================
# 11. COUNT
# =========================================================

print("========== COUNT ==========\n")

print(df.count())

print("\n")


# =========================================================
# 12. STANDARD DEVIATION
# =========================================================

print("========== STANDARD DEVIATION ==========\n")

print(df["Salary"].std())

print("\n")


# =========================================================
# 13. VARIANCE
# =========================================================

print("========== VARIANCE ==========\n")

print(df["Salary"].var())

print("\n")


# =========================================================
# 14. CORRELATION
# =========================================================

print("========== CORRELATION ==========\n")

numeric_df = df.select_dtypes(
    include="number"
)

print(numeric_df.corr())

print("\n")


# =========================================================
# 15. UNIQUE VALUES
# =========================================================

print("========== UNIQUE VALUES ==========\n")

print(df["Experience"].unique())

print("\n")


# =========================================================
# 16. VALUE COUNTS
# =========================================================

print("========== VALUE COUNTS ==========\n")

print(df["Experience"].value_counts())

print("\n")


# =========================================================
# 17. QUANTILES
# =========================================================

print("========== QUANTILES ==========\n")

print(df["Salary"].quantile([0.25, 0.50, 0.75]))

print("\n")


# =========================================================
# 18. INDEX OF MAXIMUM VALUE
# =========================================================

print("========== IDXMAX() ==========\n")

highest_salary_index = df["Salary"].idxmax()

print(highest_salary_index)

print("\n")

print("Employee With Highest Salary:\n")

print(df.loc[highest_salary_index])

print("\n")


# =========================================================
# 19. INDEX OF MINIMUM VALUE
# =========================================================

print("========== IDXMIN() ==========\n")

lowest_salary_index = df["Salary"].idxmin()

print(lowest_salary_index)

print("\n")

print("Employee With Lowest Salary:\n")

print(df.loc[lowest_salary_index])

print("\n")


# =========================================================
# 20. CUMULATIVE SUM
# =========================================================

print("========== CUMULATIVE SUM ==========\n")

df["CumulativeSalary"] = (
    df["Salary"].cumsum()
)

print(df)

print("\n")


# =========================================================
# 21. RANKING
# =========================================================

print("========== RANKING ==========\n")

df["SalaryRank"] = (
    df["Salary"].rank(
        ascending=False
    )
)

print(df)

print("\n")


# =========================================================
# 22. APPLY MULTIPLE STATISTICS
# =========================================================

print("========== MULTIPLE STATISTICS ==========\n")

print(
    df["Salary"].agg(
        ["min", "max", "mean", "sum"]
    )
)

print("\n")


# =========================================================
# 23. CHECK SKEWNESS
# =========================================================

print("========== SKEWNESS ==========\n")

print(df["Salary"].skew())

print("\n")


# =========================================================
# 24. CHECK KURTOSIS
# =========================================================

print("========== KURTOSIS ==========\n")

print(df["Salary"].kurt())

print("\n")


# =========================================================
# 25. SAMPLE DATA WITH NULL VALUES
# =========================================================

print("========== NULL VALUE STATISTICS ==========\n")

data2 = {
    "Marks": [90, 85, None, 70, 95]
}

null_df = pd.DataFrame(data2)

print(null_df)

print("\nAverage Marks:\n")

print(null_df["Marks"].mean())

print("\n")


# =========================================================
# 26. MINI PRACTICE TASK
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

students_df["Total"] = (
    students_df["Math"] +
    students_df["Science"] +
    students_df["English"]
)

students_df["Average"] = (
    students_df["Total"] / 3
)

print("UPDATED DATA:\n")

print(students_df)

print("\n")

print("CLASS AVERAGE:\n")

print(students_df["Average"].mean())

print("\n")

print("TOP STUDENT:\n")

top_student = students_df.sort_values(
    by="Total",
    ascending=False
)

print(top_student.head(1))

print("\n")


# =========================================================
# 27. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Statistics are used in:

- Machine Learning
- AI
- Business Analytics
- Data Science
- Finance

Examples:
- Average sales
- Highest revenue
- Customer behavior
- Risk analysis
- Performance tracking

Statistics are the foundation of:
- Machine Learning
- Data Analysis
"""

print("Statistics Are Extremely Important")

print("\n")


# =========================================================
# 28. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. How to find average in Pandas?

Using:
mean()

--------------------------------------------------

Q2. Difference between mean and median?

Mean:
Average value

Median:
Middle value

--------------------------------------------------

Q3. How to find maximum value?

Using:
max()

--------------------------------------------------

Q4. How to find standard deviation?

Using:
std()

--------------------------------------------------

Q5. What is correlation?

Ans:
Relationship between columns.

--------------------------------------------------

Q6. How to calculate multiple statistics?

Using:
agg()

--------------------------------------------------

Q7. Why are statistics important?

Ans:
To understand patterns and behavior
inside the dataset.
"""


# =========================================================
# 29. END OF FILE
# =========================================================

print("========== BASIC STATISTICS COMPLETED ==========")