# =========================================================
# Pandas String Operations Tutorial
# Beginner to Advanced
# File: 04_string_operations.py
# Folder: 02_Data_Cleaning
# =========================================================

# =========================================================
# 1. IMPORT PANDAS
# =========================================================

import pandas as pd

# =========================================================
# 2. WHAT ARE STRING OPERATIONS?
# =========================================================

"""
String Operations are used to:

- Clean text data
- Standardize text format
- Prepare NLP datasets
- Clean emails / names / phone numbers

Used heavily in:

- Data Cleaning
- Machine Learning
- NLP
- Business Analytics
"""

print("========== STRING OPERATIONS ==========\n")


# =========================================================
# 3. CREATE SAMPLE DATAFRAME
# =========================================================

print("========== SAMPLE DATAFRAME ==========\n")

data = {
    "Name": [
        "  mohit kumar  ",
        "AMAN SHARMA",
        "neha singh",
        "Simran KAUR",
        "rahul"
    ],

    "Email": [
        "Mohit@GMAIL.COM ",
        " aman@yahoo.com",
        "NEHA@OUTLOOK.COM",
        "simran@gmail.com ",
        " RAHUL@gmail.COM"
    ],

    "Phone": [
        "98765-43210",
        "91234 56789",
        "(99887)66554",
        "88990.11223",
        "77771-22334"
    ],

    "City": [
        " delhi ",
        "NOIDA",
        "mumbai",
        "LUCKNOW",
        " pune "
    ]
}

df = pd.DataFrame(data)

print(df)

print("\n")


# =========================================================
# 4. LOWERCASE
# =========================================================

print("========== LOWERCASE ==========\n")

df["City_Lower"] = df["City"].str.lower()

print(df["City_Lower"])

print("\n")


# =========================================================
# 5. UPPERCASE
# =========================================================

print("========== UPPERCASE ==========\n")

df["City_Upper"] = df["City"].str.upper()

print(df["City_Upper"])

print("\n")


# =========================================================
# 6. TITLE CASE
# =========================================================

print("========== TITLE CASE ==========\n")

df["Name_Title"] = df["Name"].str.title()

print(df["Name_Title"])

print("\n")


# =========================================================
# 7. REMOVE EXTRA SPACES
# =========================================================

print("========== STRIP() ==========\n")

df["Name_Clean"] = df["Name"].str.strip()

print(df["Name_Clean"])

print("\n")


# =========================================================
# 8. REPLACE VALUES
# =========================================================

print("========== REPLACE() ==========\n")

replace_city = df["City"].str.replace(
    "delhi",
    "Delhi",
    case=False
)

print(replace_city)

print("\n")


# =========================================================
# 9. CONTAINS()
# =========================================================

print("========== CONTAINS() ==========\n")

gmail_users = df[
    df["Email"].str.contains(
        "gmail",
        case=False
    )
]

print(gmail_users)

print("\n")


# =========================================================
# 10. STARTSWITH()
# =========================================================

print("========== STARTSWITH() ==========\n")

starts_with_a = df[
    df["Name"].str.lower().str.startswith("a")
]

print(starts_with_a)

print("\n")


# =========================================================
# 11. ENDSWITH()
# =========================================================

print("========== ENDSWITH() ==========\n")

ends_with_com = df[
    df["Email"].str.lower().str.endswith("com")
]

print(ends_with_com)

print("\n")


# =========================================================
# 12. SPLIT()
# =========================================================

print("========== SPLIT() ==========\n")

split_names = df["Name_Clean"].str.split()

print(split_names)

print("\n")


# =========================================================
# 13. STRING LENGTH
# =========================================================

print("========== STRING LENGTH ==========\n")

lengths = df["Name_Clean"].str.len()

print(lengths)

print("\n")


# =========================================================
# 14. CLEAN EMAILS
# =========================================================

print("========== EMAIL CLEANING ==========\n")

df["Clean_Email"] = (
    df["Email"]
    .str.strip()
    .str.lower()
)

print(df["Clean_Email"])

print("\n")


# =========================================================
# 15. CLEAN PHONE NUMBERS
# =========================================================

print("========== PHONE CLEANING ==========\n")

df["Clean_Phone"] = df["Phone"].str.replace(
    r"\D",
    "",
    regex=True
)

print(df["Clean_Phone"])

print("\n")


# =========================================================
# 16. REGEX CLEANING
# =========================================================

print("========== REGEX CLEANING ==========\n")

regex_clean = df["Phone"].str.replace(
    r"[^0-9]",
    "",
    regex=True
)

print(regex_clean)

print("\n")


# =========================================================
# 17. MULTIPLE STRING CLEANING
# =========================================================

print("========== MULTIPLE CLEANING ==========\n")

df["Final_Name"] = (
    df["Name"]
    .str.strip()
    .str.lower()
    .str.title()
)

print(df["Final_Name"])

print("\n")


# =========================================================
# 18. APPLY CLEANING PIPELINE
# =========================================================

print("========== CLEANING PIPELINE ==========\n")

df["Final_City"] = (
    df["City"]
    .str.strip()
    .str.lower()
    .str.title()
)

print(df[["City", "Final_City"]])

print("\n")


# =========================================================
# 19. NLP TEXT PREPROCESSING
# =========================================================

print("========== NLP PREPROCESSING ==========\n")

comments = pd.Series([
    "Amazing PRODUCT!!!",
    " Very GOOD Service ",
    "Bad Experience!!!"
])

clean_comments = (
    comments
    .str.lower()
    .str.strip()
    .str.replace(
        r"[^\w\s]",
        "",
        regex=True
    )
)

print(clean_comments)

print("\n")


# =========================================================
# 20. MINI PRACTICE TASK
# =========================================================

print("========== MINI PRACTICE TASK ==========\n")

student_data = {
    "Student": [
        " mohit ",
        "AMAN",
        "neha"
    ],

    "Course": [
        " data science ",
        "PYTHON",
        "machine learning"
    ]
}

students_df = pd.DataFrame(student_data)

print("ORIGINAL DATA:\n")

print(students_df)

print("\n")

students_df["Student"] = (
    students_df["Student"]
    .str.strip()
    .str.title()
)

students_df["Course"] = (
    students_df["Course"]
    .str.strip()
    .str.title()
)

print("CLEANED DATA:\n")

print(students_df)

print("\n")


# =========================================================
# 21. REAL-WORLD INDUSTRY LEARNING
# =========================================================

print("========== INDUSTRY LEARNING ==========\n")

"""
String cleaning is critical in industry.

Real-world examples:

- Customer names cleaning
- Email standardization
- NLP preprocessing
- Sentiment analysis
- Web scraping cleaning

Common Functions:

- lower()
- upper()
- strip()
- replace()
- contains()

Used in:

- Machine Learning
- NLP
- ETL Pipelines
- Business Analytics
"""

print("String Cleaning Is Industry Critical")

print("\n")


# =========================================================
# 22. INTERVIEW QUESTIONS
# =========================================================

"""
Q1. How to convert text into lowercase?

Using:
str.lower()

--------------------------------------------------

Q2. How to remove spaces?

Using:
str.strip()

--------------------------------------------------

Q3. How to replace text?

Using:
str.replace()

--------------------------------------------------

Q4. How to check substring existence?

Using:
str.contains()

--------------------------------------------------

Q5. How to split strings?

Using:
str.split()

--------------------------------------------------

Q6. How to clean phone numbers?

Using Regex:

r"\D"

--------------------------------------------------

Q7. Why string operations matter in ML?

Because real datasets contain:

- dirty text
- inconsistent formatting
- noisy values
"""


# =========================================================
# 23. END OF FILE
# =========================================================

print("========== STRING OPERATIONS COMPLETED ==========")