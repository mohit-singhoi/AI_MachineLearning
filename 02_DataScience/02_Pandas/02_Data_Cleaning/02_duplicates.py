# =========================================================
# Pandas Duplicate Data Handling Tutorial
# Beginner to Advanced
# File: 02_duplicates.py
# Folder: 02_Data_Cleaning
# =========================================================


# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT ARE DUPLICATES?
# =========================================================

"""
Duplicate Data means:

- Repeated rows
- Same records appearing multiple times

Problems Caused:
- Incorrect analysis
- Wrong ML predictions
- Increased dataset size

Very common in:
- Customer datasets
- Sales datasets
- Employee records
- Web scraping data
"""

print("========== DUPLICATE DATA ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": [
        "Mohit",
        "Aman",
        "Neha",
        "Mohit",
        "Simran",
        "Aman"
    ],
    "Department": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "Marketing",
        "HR"
    ],
    "Salary": [
        50000,
        60000,
        55000,
        50000,
        70000,
        60000
    ]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. CHECK DUPLICATE ROWS
# =========================================================

print("========== CHECK DUPLICATES ==========\n")

duplicates = df.duplicated()

print(duplicates)

print("\n")


# =========================================================
# 5. SHOW ONLY DUPLICATE ROWS
# =========================================================

print("========== ONLY DUPLICATE ROWS ==========\n")

duplicate_rows = df[
    df.duplicated()
]

print(duplicate_rows)

print("\n")


# =========================================================
# 6. COUNT DUPLICATE ROWS
# =========================================================

print("========== DUPLICATE COUNT ==========\n")

duplicate_count = df.duplicated().sum()

print(duplicate_count)

print("\n")


# =========================================================
# 7. REMOVE DUPLICATE ROWS
# =========================================================

print("========== REMOVE DUPLICATES ==========\n")

removed_duplicates = df.drop_duplicates()

print(removed_duplicates)

print("\n")


# =========================================================
# 8. KEEP LAST DUPLICATE
# =========================================================

print("========== KEEP LAST DUPLICATE ==========\n")

keep_last = df.drop_duplicates(
    keep="last"
)

print(keep_last)

print("\n")


# =========================================================
# 9. REMOVE ALL DUPLICATES
# =========================================================

print("========== REMOVE ALL DUPLICATES ==========\n")

remove_all = df.drop_duplicates(
    keep=False
)

print(remove_all)

print("\n")


# =========================================================
# 10. DUPLICATES BASED ON SINGLE COLUMN
# =========================================================

print("========== DUPLICATES BASED ON NAME ==========\n")

name_duplicates = df.duplicated(
    subset=["Name"]
)

print(name_duplicates)

print("\n")


# =========================================================
# 11. REMOVE DUPLICATES USING SINGLE COLUMN
# =========================================================

print("========== REMOVE DUPLICATES USING NAME ==========\n")

unique_names = df.drop_duplicates(
    subset=["Name"]
)

print(unique_names)

print("\n")


# =========================================================
# 12. KEEP LAST USING SINGLE COLUMN
# =========================================================

print("========== KEEP LAST NAME ==========\n")

last_name = df.drop_duplicates(
    subset=["Name"],
    keep="last"
)

print(last_name)

print("\n")


# =========================================================
# 13. DUPLICATES USING MULTIPLE COLUMNS
# =========================================================

print("========== MULTIPLE COLUMN DUPLICATES ==========\n")

multi_duplicates = df.duplicated(
    subset=["Name", "Department"]
)

print(multi_duplicates)

print("\n")


# =========================================================
# 14. FIND ALL DUPLICATE RECORDS
# =========================================================

print("========== ALL DUPLICATE RECORDS ==========\n")

all_duplicates = df[
    df.duplicated(keep=False)
]

print(all_duplicates)

print("\n")


# =========================================================
# 15. ADD DUPLICATE ROWS
# =========================================================

print("========== ADD DUPLICATE ROWS ==========\n")

new_row = pd.DataFrame({
    "Name": ["Mohit"],
    "Department": ["IT"],
    "Salary": [50000]
})

updated_df = pd.concat(
    [df, new_row],
    ignore_index=True
)

print(updated_df)

print("\n")


# =========================================================
# 16. REMOVE DUPLICATES AFTER CONCAT
# =========================================================

print("========== CLEAN CONCAT DATA ==========\n")

cleaned_df = updated_df.drop_duplicates()

print(cleaned_df)

print("\n")


# =========================================================
# 17. RESET INDEX AFTER CLEANING
# =========================================================

print("========== RESET INDEX ==========\n")

reset_df = cleaned_df.reset_index(
    drop=True
)

print(reset_df)

print("\n")


# =========================================================
# 18. CHECK UNIQUE VALUES
# =========================================================

print("========== UNIQUE VALUES ==========\n")

print(df["Name"].unique())

print("\n")


# =========================================================
# 19. COUNT UNIQUE VALUES
# =========================================================

print("========== UNIQUE VALUE COUNT ==========\n")

print(df["Name"].nunique())

print("\n")


# =========================================================
# 20. VALUE COUNTS
# =========================================================

print("========== VALUE COUNTS ==========\n")

print(df["Name"].value_counts())

print("\n")


# =========================================================
# 21. SORT BEFORE REMOVING DUPLICATES
# =========================================================

print("========== SORT BEFORE CLEANING ==========\n")

sorted_df = df.sort_values(
    by="Salary",
    ascending=False
)

print(sorted_df)

print("\n")


# =========================================================
# 22. REMOVE DUPLICATES FROM SORTED DATA
# =========================================================

print("========== CLEAN SORTED DATA ==========\n")

sorted_clean = sorted_df.drop_duplicates(
    subset=["Name"]
)

print(sorted_clean)

print("\n")


# =========================================================
# 23. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {
    "Student": [
        "Rahul",
        "Mohit",
        "Neha",
        "Rahul",
        "Aman"
    ],
    "Marks": [
        90,
        85,
        95,
        90,
        70
    ]
}

students_df = pd.DataFrame(student_data)

print("ORIGINAL DATA:\n")

print(students_df)

print("\n")

print("DUPLICATE ROWS:\n")

print(
    students_df[
        students_df.duplicated()
    ]
)

print("\n")

print("AFTER REMOVING DUPLICATES:\n")

clean_students = students_df.drop_duplicates()

print(clean_students)

print("\n")


# =========================================================
# 24. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Duplicate handling is one of the
most important data cleaning tasks.

In real-world projects:
- Duplicate customers exist
- Duplicate transactions exist
- Duplicate scraped records exist

Common solutions:
- drop_duplicates()
- unique()
- value_counts()

Used heavily in:
- Data Science
- Machine Learning
- Business Analytics
- ETL Pipelines
"""

print("Duplicate Handling Is Industry Critical")

print("\n")


# =========================================================
# 25. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. What are duplicate values?

Ans:
Repeated records in a dataset.

--------------------------------------------------

Q2. How to detect duplicates?

Using:
duplicated()

--------------------------------------------------

Q3. How to remove duplicates?

Using:
drop_duplicates()

--------------------------------------------------

Q4. What does keep='last' mean?

Ans:
Keeps last duplicate row.

--------------------------------------------------

Q5. How to remove all duplicates?

Using:
keep=False

--------------------------------------------------

Q6. How to check unique values?

Using:
unique()

--------------------------------------------------

Q7. Difference between unique() and nunique()?

unique():
Returns unique values

nunique():
Returns count of unique values

--------------------------------------------------

Q8. Why duplicate handling is important?

Ans:
Because duplicates create incorrect
analysis and ML predictions.
"""


# =========================================================
# 26. END OF FILE
# =========================================================

print("========== DUPLICATE HANDLING COMPLETED ==========")