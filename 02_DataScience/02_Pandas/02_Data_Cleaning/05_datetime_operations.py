# =========================================================
# Pandas DateTime Operations Tutorial
# Beginner to Advanced
# File: 05_datetime_operations.py
# Folder: 02_Data_Cleaning
# =========================================================


# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT ARE DATETIME OPERATIONS?
# =========================================================

"""
Datetime Operations are used for:

- Date Cleaning
- Time Analysis
- Sales Analysis
- Time Series Data
- Machine Learning

Used In:

- Finance
- Banking
- E-commerce
- Data Science
- Deep Learning
"""

print("========== DATETIME OPERATIONS ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Customer": [
        "Mohit",
        "Aman",
        "Neha",
        "Simran",
        "Rahul"
    ],

    "OrderDate": [
        "2025-01-15",
        "2025-02-20",
        "2025-03-10",
        "2025-04-05",
        "2025-05-18"
    ],

    "Sales": [
        5000,
        8000,
        6500,
        9200,
        7100
    ]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. CHECK DATATYPES
# =========================================================

print("========== DATATYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 5. CONVERT TO DATETIME
# =========================================================

print("========== TO_DATETIME() ==========\n")

df["OrderDate"] = pd.to_datetime(
    df["OrderDate"]
)

print(df)

print("\n")

print(df.dtypes)

print("\n")


# =========================================================
# 6. EXTRACT YEAR
# =========================================================

print("========== EXTRACT YEAR ==========\n")

df["Year"] = df["OrderDate"].dt.year

print(df[["OrderDate", "Year"]])

print("\n")


# =========================================================
# 7. EXTRACT MONTH
# =========================================================

print("========== EXTRACT MONTH ==========\n")

df["Month"] = df["OrderDate"].dt.month

print(df[["OrderDate", "Month"]])

print("\n")


# =========================================================
# 8. EXTRACT DAY
# =========================================================

print("========== EXTRACT DAY ==========\n")

df["Day"] = df["OrderDate"].dt.day

print(df[["OrderDate", "Day"]])

print("\n")


# =========================================================
# 9. EXTRACT DAY NAME
# =========================================================

print("========== DAY NAME ==========\n")

df["DayName"] = df["OrderDate"].dt.day_name()

print(df[["OrderDate", "DayName"]])

print("\n")


# =========================================================
# 10. EXTRACT WEEKDAY
# =========================================================

print("========== WEEKDAY ==========\n")

df["Weekday"] = df["OrderDate"].dt.weekday

print(df[["OrderDate", "Weekday"]])

print("\n")


# =========================================================
# 11. EXTRACT QUARTER
# =========================================================

print("========== QUARTER ==========\n")

df["Quarter"] = df["OrderDate"].dt.quarter

print(df[["OrderDate", "Quarter"]])

print("\n")


# =========================================================
# 12. CURRENT DATE & TIME
# =========================================================

print("========== CURRENT DATETIME ==========\n")

current_time = pd.Timestamp.now()

print(current_time)

print("\n")


# =========================================================
# 13. DATE FILTERING
# =========================================================

print("========== DATE FILTERING ==========\n")

filtered = df[
    df["OrderDate"] > "2025-03-01"
]

print(filtered)

print("\n")


# =========================================================
# 14. DATE DIFFERENCE
# =========================================================

print("========== DATE DIFFERENCE ==========\n")

df["DaysPassed"] = (
    current_time -
    df["OrderDate"]
).dt.days

print(df[["OrderDate", "DaysPassed"]])

print("\n")


# =========================================================
# 15. ADD DAYS
# =========================================================

print("========== ADD DAYS ==========\n")

df["NextWeek"] = (
    df["OrderDate"] +
    pd.Timedelta(days=7)
)

print(df[["OrderDate", "NextWeek"]])

print("\n")


# =========================================================
# 16. SUBTRACT DAYS
# =========================================================

print("========== SUBTRACT DAYS ==========\n")

df["PreviousWeek"] = (
    df["OrderDate"] -
    pd.Timedelta(days=7)
)

print(df[["OrderDate", "PreviousWeek"]])

print("\n")


# =========================================================
# 17. SORT BY DATE
# =========================================================

print("========== SORT BY DATE ==========\n")

sorted_df = df.sort_values(
    by="OrderDate",
    ascending=False
)

print(sorted_df)

print("\n")


# =========================================================
# 18. FORMAT DATE
# =========================================================

print("========== DATE FORMAT ==========\n")

formatted = df["OrderDate"].dt.strftime(
    "%d-%m-%Y"
)

print(formatted)

print("\n")


# =========================================================
# 19. HANDLE INVALID DATES
# =========================================================

print("========== INVALID DATES ==========\n")

bad_dates = pd.Series([
    "2025-01-10",
    "WrongDate",
    "2025-04-12"
])

converted = pd.to_datetime(
    bad_dates,
    errors="coerce"
)

print(converted)

print("\n")


# =========================================================
# 20. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

sales_data = {
    "Date": [
        "2025-01-01",
        "2025-02-15",
        "2025-03-20"
    ],

    "Revenue": [
        50000,
        70000,
        90000
    ]
}

sales_df = pd.DataFrame(sales_data)

sales_df["Date"] = pd.to_datetime(
    sales_df["Date"]
)

sales_df["Month"] = (
    sales_df["Date"].dt.month_name()
)

print(sales_df)

print("\n")


# =========================================================
# 21. TIME SERIES BASICS
# =========================================================

print("========== TIME SERIES ==========\n")

ts = pd.date_range(
    start="2025-01-01",
    periods=5,
    freq="D"
)

print(ts)

print("\n")


# =========================================================
# 22. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Datetime handling is extremely important.

Real-world Uses:

- Sales Analysis
- Stock Market Data
- Banking Transactions
- User Activity Tracking
- Machine Learning Features

Common Functions:

- to_datetime()
- dt.year
- dt.month
- Timedelta()
- Timestamp.now()

Used heavily in:

- Data Science
- Deep Learning
- Business Analytics
- Forecasting
"""

print("Datetime Handling Is Industry Critical")

print("\n")


# =========================================================
# 23. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. How to convert string to datetime?

Using:

pd.to_datetime()

--------------------------------------------------

Q2. How to extract year?

Using:

.dt.year

--------------------------------------------------

Q3. How to extract month?

Using:

.dt.month

--------------------------------------------------

Q4. How to handle invalid dates?

Using:

errors='coerce'

--------------------------------------------------

Q5. What is Timedelta?

Used for:

Date addition/subtraction.

--------------------------------------------------

Q6. How to get current datetime?

Using:

pd.Timestamp.now()

--------------------------------------------------

Q7. Why datetime operations are important?

Because many real datasets contain:

- timestamps
- sales dates
- transaction dates
- event logs
"""


# =========================================================
# 24. END OF FILE
# =========================================================

print("========== DATETIME OPERATIONS COMPLETED ==========")