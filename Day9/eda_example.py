# ----------------------------------------------------------
# STEP 1 — Import Required Libraries
# ----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Improve plot appearance
sns.set(style="whitegrid")

# ----------------------------------------------------------
# STEP 2 — Load CSV File
# ----------------------------------------------------------

# Find the folder where this Python file is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Create path for data.csv
file_path = os.path.join(folder_path, "data.csv")

# Read CSV file
df = pd.read_csv(file_path)
print("\nCSV file loaded successfully!")

# ----------------------------------------------------------
# TOPIC 1 — DATASET INSPECTION
# ----------------------------------------------------------

print("\n===== FIRST 5 ROWS =====")
print(df.head())
print("\n===== LAST 5 ROWS =====")
print(df.tail())
print("\n===== DATASET SHAPE =====")
print(df.shape)
print("\n===== DATASET INFORMATION =====")
df.info()
print("\n===== SUMMARY STATISTICS =====")
print("description:",df.describe())
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# ----------------------------------------------------------
# TOPIC 2 — UNIVARIATE ANALYSIS
# ----------------------------------------------------------

# 1. Histogram — Age

plt.figure(figsize=(7, 5))

sns.histplot(
    df["Age"],
    kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")


# 2. Histogram — Salary

plt.figure(figsize=(7, 5))

sns.histplot(
    df["Salary"],
    kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")


# 3. Boxplot — Salary

plt.figure(figsize=(7, 4))

sns.boxplot(
    x=df["Salary"]
)

plt.title("Salary Boxplot")
plt.xlabel("Salary")


# 4. Department counts

print("\n===== DEPARTMENT COUNTS =====")
print(df["Department"].value_counts())


# 5. Gender counts

print("\n===== GENDER COUNTS =====")
print(df["Gender"].value_counts())


# 6. Bar plot — Department

plt.figure(figsize=(7, 5))

sns.countplot(
    x="Department",
    data=df
)

plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")


# ----------------------------------------------------------
# TOPIC 3 — BIVARIATE ANALYSIS
# ----------------------------------------------------------

# 1. Age vs Salary

plt.figure(figsize=(7, 5))

sns.scatterplot(
    x="Age",
    y="Salary",
    data=df
)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")


# 2. Experience vs Salary

plt.figure(figsize=(7, 5))

sns.scatterplot(
    x="Experience",
    y="Salary",
    data=df
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")


# 3. Salary by Gender

plt.figure(figsize=(7, 5))

sns.boxplot(
    x="Gender",
    y="Salary",
    data=df
)

plt.title("Salary by Gender")
plt.xlabel("Gender")
plt.ylabel("Salary")


# 4. Salary by Department

plt.figure(figsize=(7, 5))

sns.boxplot(
    x="Department",
    y="Salary",
    data=df)
plt.title("Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")


# ----------------------------------------------------------
# TOPIC 4 — CORRELATION ANALYSIS
# ----------------------------------------------------------

corr_matrix = df.corr(numeric_only=True)

print("\n===== CORRELATION MATRIX =====")
print(corr_matrix)


# Correlation heatmap

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")


# ----------------------------------------------------------
# TOPIC 5 — OUTLIER DETECTION
# ----------------------------------------------------------

# Age outliers

plt.figure(figsize=(7, 4))

sns.boxplot(
    x=df["Age"])

plt.title("Age Outliers")
plt.xlabel("Age")


# Experience outliers

plt.figure(figsize=(7, 4))

sns.boxplot(
    x=df["Experience"])

plt.title("Experience Outliers")
plt.xlabel("Experience")


# ----------------------------------------------------------
# FINAL STEP — SAMPLE INSIGHTS
# ----------------------------------------------------------

print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary generally increases with Experience and Age.")
print("2. Finance department shows a higher salary range.")
print("3. No extreme outliers are visible in Age or Experience.")
print("4. Gender distribution is relatively balanced.")
print("5. Experience has a strong positive relationship with Salary.")
print("\n===== DISPLAYING ALL GRAPHS =====")
plt.show()


# ==========================================================
# END OF EDA SCRIPT
# ==========================================================

print("\n===== EDA PROGRAM COMPLETED SUCCESSFULLY =====")