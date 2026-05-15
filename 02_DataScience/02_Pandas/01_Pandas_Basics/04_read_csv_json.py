# # =========================================================
# # Pandas Read CSV & JSON
# # Beginner to Advanced
# # File: 04_read_csv_json.py
# # =========================================================

# # =========================================================
# # 1. IMPORT PANDAS and PATH for dynamic Path
# # =========================================================

from pathlib import Path
import pandas as pd


# # =========================================================
# # 2. WHAT IS CSV?
# # =========================================================

# """
# CSV = Comma Separated Values

# - Stores tabular data
# - Most common dataset format in Data Science
# - Used in:
#     • Machine Learning
#     • Data Analysis
#     • Business Analytics
# """

# print("========== CSV FILES ==========\n")


# # =========================================================
# # 3. READ CSV FILE
# # =========================================================


# print("========== READ CSV FILE  AS A BEGINEER LEVEL ==========\n")

# # Reading employees dataset
# df = pd.read_csv("../datasets/employees.csv")

# print(df)

# print("\n")



# USED FOR FETCHING DYNAMIC PATH LOOKS LIKE REALWORLD/INDUSTRY REALATED WORK

import pandas as pd

# Current file directory
BASE_DIR = Path(__file__).resolve().parent

# Dataset path
csv_path = BASE_DIR.parent / "datasets" / "employees.csv"

print(csv_path)

df = pd.read_csv(csv_path)


print(df)
print("\n")


# =========================================================
# 4. FIRST 5 ROWS
# =========================================================

print("========== HEAD() ==========\n")

print(df.head())

print("\n")


# =========================================================
# 5. LAST 5 ROWS
# =========================================================

print("========== TAIL() ==========\n")

print(df.tail())

print("\n")


# =========================================================
# 6. SHAPE OF DATASET
# =========================================================

print("========== SHAPE ==========\n")

print(df.shape)

print("\n")


# =========================================================
# 7. COLUMN NAMES
# =========================================================

print("========== COLUMNS ==========\n")

print(df.columns)

print("\n")


# =========================================================
# 8. DATA TYPES
# =========================================================

print("========== DATA TYPES ==========\n")

print(df.dtypes)

print("\n")


# =========================================================
# 9. DATASET INFORMATION
# =========================================================

print("========== INFO ==========\n")

print(df.info())

print("\n")


# =========================================================
# 10. DESCRIBE DATA
# =========================================================

print("========== DESCRIBE ==========\n")

print(df.describe())

print("\n")


# =========================================================
# 11. READ SPECIFIC COLUMNS
# =========================================================

print("========== SPECIFIC COLUMNS ==========\n")

## Begineer level
# selected_columns = pd.read_csv(
#     "datasets/employees.csv",
#     usecols=["Name", "Salary"]
# )

selected_columns = pd.read_csv(
    csv_path,
    usecols=["EmployeeName", "Salary"]
)


print(selected_columns)

print("\n")


# =========================================================
# 12. READ LIMITED ROWS
# =========================================================

print("========== LIMITED ROWS ==========\n")

# limited_rows = pd.read_csv(
#     "datasets/employees.csv",
#     nrows=5
# )

limited_rows = pd.read_csv(
    csv_path,
    nrows=5
)


print(limited_rows)

print("\n")


# =========================================================
# 13. SKIP ROWS
# =========================================================

print("========== SKIP ROWS ==========\n")

skip_rows = pd.read_csv(
    csv_path,
    skiprows=2
)

print(skip_rows)

print("\n")


# =========================================================
# 14. CUSTOM COLUMN NAMES
# =========================================================

print("========== CUSTOM COLUMN NAMES ==========\n")

custom_df = pd.read_csv(csv_path)

custom_df.columns = [
    "ID",
    "EmployeeName",
    "EmployeeAge",
    "Department",
    "Location",
    "Salary",
    "Experience"
]

print(custom_df)

print("\n")


# =========================================================
# 15. SAVE DATAFRAME AS CSV
# =========================================================

print("========== SAVE CSV ==========\n")

custom_df.to_csv(
    csv_path,
    index=False
)

print("CSV File Saved Successfully")

print("\n")

print(df.columns)
# =========================================================
# 16. FILTER DATA
# =========================================================

# print("========== FILTER DATA ==========\n")

high_salary = df[df["Salary"] > 60000]

print(high_salary)

print("\n")


# =========================================================
# 17. SORT DATA
# =========================================================

print("========== SORT DATA ==========\n")

sorted_df = df.sort_values(
    by="Salary",
    ascending=False
)

print(sorted_df)

print("\n")


# =========================================================
# 18. CHECK NULL VALUES
# =========================================================

print("========== NULL VALUES ==========\n")

print(df.isnull())

print("\n")


# =========================================================
# 19. COUNT NULL VALUES
# =========================================================

print("========== NULL VALUE COUNT ==========\n")

print(df.isnull().sum())

print("\n")


# =========================================================
# 20. REMOVE DUPLICATES
# =========================================================

print("========== REMOVE DUPLICATES ==========\n")

duplicate_removed = df.drop_duplicates()

print(duplicate_removed)

print("\n")


# =========================================================
# 21. WHAT IS JSON?
# =========================================================

"""
JSON = JavaScript Object Notation

- Used in APIs
- Stores data in key-value format
- Common in web applications
"""

print("========== JSON FILES ==========\n")


# =========================================================
# 22. READ JSON FILE
# =========================================================



# print("JSON FILE Path")

BASE_DIR = Path(__file__).resolve().parent

json_path = BASE_DIR.parent / "datasets" / "employees.json"

print("========== READ JSON ==========\n")

json_df = pd.read_json(json_path)

print(json_df)

print("\n")


# =========================================================
# 23. JSON HEAD
# =========================================================

print("========== JSON HEAD ==========\n")

print(json_df.head())

print("\n")


# =========================================================
# 24. JSON SHAPE
# =========================================================

print("========== JSON SHAPE ==========\n")

print(json_df.shape)

print("\n")


# =========================================================
# 25. JSON INFO
# =========================================================

print("========== JSON INFO ==========\n")

print(json_df.info())

print("\n")


# =========================================================
# 26. CREATE DATAFRAME FROM DICTIONARY
# =========================================================

print("========== DATAFRAME FROM DICTIONARY ==========\n")

data = {
    "Name": ["Rahul", "Mohit", "Neha"],
    "Math": [90, 85, 95],
    "Science": [88, 91, 89]
}

students_df = pd.DataFrame(data)

print(students_df)

print("\n")


# =========================================================
# 27. SAVE DATAFRAME AS JSON
# =========================================================

output_json_path = BASE_DIR.parent / "datasets" / "students_output.json"

print("========== SAVE JSON ==========\n")

## Begineer Level
# students_df.to_json(
#     "datasets/students_output.json"
# )

students_df.to_json(
    output_json_path,
    orient="records",
    indent=4
)

print("JSON File Saved Successfully")

print("\n")


# =========================================================
# 28. CSV TO JSON
# =========================================================

print("========== CSV TO JSON ==========\n")

# CSV INPUT PATH
csv_path1 = BASE_DIR.parent / "datasets" / "sales_data.csv"

# JSON OUTPUT PATH
json_output_path = BASE_DIR.parent / "datasets" / "sales_data.json"

# READ CSV
sales_df = pd.read_csv(csv_path1)

# CONVERT CSV TO JSON
sales_df.to_json(
    json_output_path,
    orient="records",
    indent=4
)

print("CSV Converted To JSON")

print("\n")

# =========================================================
# 29. JSON TO CSV
# =========================================================

print("========== JSON TO CSV ==========\n")

# JSON INPUT PATH
json_input_path = BASE_DIR.parent / "datasets" / "students.json"

# CSV OUTPUT PATH
csv_output_path = BASE_DIR.parent / "datasets" / "students_output.csv"

# READ JSON FILE
students_json = pd.read_json(json_input_path)

# CONVERT JSON TO CSV
students_json.to_csv(
    csv_output_path,
    index=False
)

print("JSON Converted To CSV")

print("\n")


# =========================================================
# 30. READ EXCEL FILE
# =========================================================

print("========== READ EXCEL ==========\n")

"""
Syntax:

pd.read_excel("file.xlsx")
"""

# EXCEL FILE PATH
excel_path = BASE_DIR.parent / "datasets" / "employees.xlsx"

# READ EXCEL FILE
excel_df = pd.read_excel(excel_path)

print(excel_df)

print("\n")


# =========================================================
# 31. EXPORT TO EXCEL
# =========================================================

print("========== EXPORT TO EXCEL ==========\n")

# EXCEL OUTPUT PATH
excel_output_path = BASE_DIR.parent / "datasets" / "employees.xlsx"

# EXPORT DATAFRAME TO EXCEL
df.to_excel(
    excel_output_path,
    index=False
)

print("Excel File Exported")

print("\n")


# =========================================================
# 32. LARGE DATASET HANDLING
# =========================================================

print("========== LARGE DATASETS ==========\n")

"""
Useful Parameters:

- chunksize
- low_memory
- nrows
- usecols
"""

# DATASET PATH
large_csv_path = BASE_DIR.parent / "datasets" / "large_sales_data.csv"

# =========================================================
# 1. READ ONLY FIRST 5 ROWS
# =========================================================

sample_df = pd.read_csv(
    large_csv_path,
    nrows=5
)

print("FIRST 5 ROWS:\n")
print(sample_df)

print("\n")

# =========================================================
# 2. READ SPECIFIC COLUMNS ONLY
# =========================================================

selected_df = pd.read_csv(
    large_csv_path,
    usecols=["Product", "Sales"]
)

print("SELECTED COLUMNS:\n")
print(selected_df.head())

print("\n")

# =========================================================
# 3. HANDLE LARGE FILES USING CHUNKS
# =========================================================

print("READING IN CHUNKS:\n")

chunk_iterator = pd.read_csv(
    large_csv_path,
    chunksize=1000
)

for chunk in chunk_iterator:
    print(chunk.head())
    break

print("\n")

# =========================================================
# 4. LOW MEMORY MODE
# =========================================================

low_memory_df = pd.read_csv(
    large_csv_path,
    low_memory=False
)

print("LOW MEMORY MODE ENABLED")

print("\n")


# =========================================================
# 33. MINI PRACTICE TASK
# =========================================================

# Netflix Dynamic Path 
netflixpath = BASE_DIR.parent / "datasets" / "netflix_data.csv"

print("========== MINI PRACTICE TASK ==========\n")

netflix_df = pd.read_csv(
    netflixpath
)

print(netflix_df.head())

print("\n")

print("Only Movies:\n")

movies = netflix_df[
    netflix_df["Type"] == "Movie"
]

print(movies)

print("\n")

print("Top Rated Content:\n")

top_rated = netflix_df.sort_values(
    by="Rating",
    ascending=False
)

print(top_rated.head())

print("\n")


# =========================================================
# 34. MINI PROJECT TASK
# =========================================================

print("========== MINI PROJECT TASK ==========\n")

# SALES DATASET PATH
salespath = BASE_DIR.parent / "datasets" / "sales_data.csv"

# READ CSV FILE
sales_df = pd.read_csv(salespath)

print("ORIGINAL DATA:\n")

print(sales_df.head())

print("\n")

# =========================================================
# TOTAL SALES CALCULATION
# =========================================================

print("TOTAL SALES:\n")

sales_df["TotalAmount"] = (
    sales_df["Quantity"] *
    sales_df["Price"]
)

print(sales_df.head())

print("\n")

# =========================================================
# HIGHEST SALES PRODUCT
# =========================================================

print("HIGHEST SALES PRODUCT:\n")

highest_sales = sales_df.sort_values(
    by="TotalAmount",
    ascending=False
)

print(highest_sales.head(1))

print("\n")


# # =========================================================
# # 35. INTERVIEW QUESTIONS
# # =========================================================

# """
# Q1. What is CSV?

# A file format used to store tabular data.

# --------------------------------------------------

# Q2. How to read CSV file?

# Using:
# pd.read_csv()

# --------------------------------------------------

# Q3. How to read JSON file?

# Using:
# pd.read_json()

# --------------------------------------------------

# Q4. How to export CSV?

# Using:
# df.to_csv()

# --------------------------------------------------

# Q5. How to export JSON?

# Using:
# df.to_json()

# --------------------------------------------------

# Q6. How to check dataset information?

# Using:
# df.info()

# --------------------------------------------------

# Q7. How to check null values?

# Using:
# df.isnull()

# --------------------------------------------------

# Q8. How to remove duplicate rows?

# Using:
# drop_duplicates()

# --------------------------------------------------

# Q9. Why is CSV important in ML?

# Because most datasets are stored in CSV format.

# --------------------------------------------------

# Q10. What is JSON mainly used for?

# - APIs
# - Web Applications
# - Data Exchange
# """

# # =========================================================
# # 36. END OF FILE
# # =========================================================

# print("========== CSV & JSON TUTORIAL COMPLETED ==========")