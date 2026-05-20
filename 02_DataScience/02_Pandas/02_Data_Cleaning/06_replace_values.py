# =========================================================
# Pandas Replace Values Tutorial
# Beginner to Advanced
# File: 06_replace_values.py
# Folder: 02_Data_Cleaning
# =========================================================


# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd


# =========================================================
# 2. WHAT IS VALUE REPLACEMENT?
# =========================================================

"""
Value Replacement means:

Changing existing values
into new values.

Used For:

- Data Cleaning
- Standardization
- Missing Value Fixing
- Text Cleaning
- ML Preprocessing

Common Methods:

- replace()
- map()
- where()
"""

print("========== VALUE REPLACEMENT ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": [
        "Mohit",
        "Aman",
        "Neha",
        "Rahul",
        "Simran"
    ],

    "Department": [
        "IT",
        "HR",
        "IT",
        "Finance",
        "HR"
    ],

    "Salary": [
        50000,
        60000,
        55000,
        70000,
        65000
    ],

    "Gender": [
        "M",
        "M",
        "F",
        "M",
        "F"
    ]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. REPLACE SINGLE VALUE
# =========================================================

print("========== REPLACE SINGLE VALUE ==========\n")

single_replace = df.replace(
    "IT",
    "Information Technology"
)

print(single_replace)

print("\n")


# =========================================================
# 5. REPLACE MULTIPLE VALUES
# =========================================================

print("========== MULTIPLE VALUE REPLACEMENT ==========\n")

multiple_replace = df.replace({

    "IT": "Tech",

    "HR": "Human Resource"

})

print(multiple_replace)

print("\n")


# =========================================================
# 6. COLUMN SPECIFIC REPLACEMENT
# =========================================================

print("========== COLUMN SPECIFIC REPLACE ==========\n")

column_replace = df.replace({

    "Gender": {

        "M": "Male",

        "F": "Female"
    }

})

print(column_replace)

print("\n")


# =========================================================
# 7. REPLACE USING LIST
# =========================================================

print("========== LIST REPLACEMENT ==========\n")

list_replace = df["Department"].replace(

    ["IT", "HR"],

    ["Technology", "Human Resource"]

)

print(list_replace)

print("\n")


# =========================================================
# 8. REPLACE NUMERIC VALUES
# =========================================================

print("========== NUMERIC REPLACEMENT ==========\n")

salary_replace = df["Salary"].replace(

    50000,

    52000

)

print(salary_replace)

print("\n")


# =========================================================
# 9. REPLACE USING DICTIONARY
# =========================================================

print("========== DICTIONARY REPLACEMENT ==========\n")

dept_mapping = {

    "IT": "Technology",

    "HR": "Human Resource",

    "Finance": "Accounts"
}

dictionary_replace = df["Department"].replace(
    dept_mapping
)

print(dictionary_replace)

print("\n")


# =========================================================
# 10. MAP FUNCTION
# =========================================================

print("========== MAP FUNCTION ==========\n")

df["GenderFull"] = df["Gender"].map({

    "M": "Male",

    "F": "Female"

})

print(df)

print("\n")


# =========================================================
# 11. CONDITIONAL REPLACEMENT
# =========================================================

print("========== CONDITIONAL REPLACEMENT ==========\n")

df["SalaryStatus"] = df["Salary"].where(

    df["Salary"] >= 60000,

    "Low Salary"
)

print(df)

print("\n")


# =========================================================
# 12. REPLACE NULL VALUES
# =========================================================

print("========== NULL VALUE REPLACE ==========\n")

null_data = {

    "Name": [
        "Mohit",
        None,
        "Neha"
    ],

    "Marks": [
        90,
        None,
        85
    ]
}

null_df = pd.DataFrame(null_data)

print("ORIGINAL DATA:\n")

print(null_df)

print("\n")

filled_df = null_df.replace(
    None,
    "Missing"
)

print("AFTER REPLACEMENT:\n")

print(filled_df)

print("\n")


# =========================================================
# 13. REGEX REPLACEMENT
# =========================================================

print("========== REGEX REPLACEMENT ==========\n")

city_df = pd.DataFrame({

    "City": [

        "Delhi123",

        "Mumbai456",

        "Noida789"
    ]
})

clean_city = city_df.replace(

    r"\d+",

    "",

    regex=True
)

print(clean_city)

print("\n")


# =========================================================
# 14. INPLACE REPLACEMENT
# =========================================================

print("========== INPLACE REPLACE ==========\n")

df.replace(

    "HR",

    "Human Resource",

    inplace=True
)

print(df)

print("\n")


# =========================================================
# 15. CASE STANDARDIZATION
# =========================================================

print("========== STANDARDIZATION ==========\n")

country_df = pd.DataFrame({

    "Country": [

        "india",

        "INDIA",

        "India",

        "usa",

        "USA"
    ]
})

country_df["Country"] = (

    country_df["Country"]

    .str.upper()
)

print(country_df)

print("\n")


# =========================================================
# 16. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {

    "Student": [

        "Rahul",

        "Mohit",

        "Neha"

    ],

    "Result": [

        "P",

        "F",

        "P"
    ]
}

students_df = pd.DataFrame(
    student_data
)

print("ORIGINAL DATA:\n")

print(students_df)

print("\n")

students_df["Result"] = (

    students_df["Result"]

    .replace({

        "P": "Pass",

        "F": "Fail"

    })
)

print("UPDATED DATA:\n")

print(students_df)

print("\n")


# =========================================================
# 17. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
Value Replacement is critical
in real-world datasets.

Examples:

Male / M / male
→ standardized to Male

Country names:
India / INDIA / india
→ standardized.

Missing values:
NULL
→ Unknown

Used heavily in:

- Machine Learning
- NLP
- Data Cleaning
- ETL Pipelines
- Analytics
"""

print("Replacement Is Industry Critical")

print("\n")


# =========================================================
# 18. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. How to replace values?

Using:

replace()

--------------------------------------------------

Q2. How to replace multiple values?

Using dictionary.

--------------------------------------------------

Q3. What is map()?

Used for value mapping.

--------------------------------------------------

Q4. How to replace using regex?

Using:

regex=True

--------------------------------------------------

Q5. Difference between replace() and map()?

replace():
General purpose.

map():
Mostly column mapping.

--------------------------------------------------

Q6. Why standardization is important?

Because inconsistent values
break analysis and ML models.
"""


# =========================================================
# 19. END OF FILE
# =========================================================

print("========== REPLACE VALUES COMPLETED ==========")