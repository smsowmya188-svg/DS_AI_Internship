import pandas as pd

# 1. Read the CSV file
df = pd.read_csv("Day7/task1/students.csv")

# 2. Display original dataset
print("\n========== ORIGINAL DATASET ==========")
print(df)

# 3. Find shape of original dataset
print("\n========== ORIGINAL SHAPE ==========")
print(df.shape)

# 4. Identify missing values in each column
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 5. Count total missing values
print("\n========== TOTAL MISSING VALUES ==========")
print(df.isnull().sum().sum())

# 6. Detect duplicate records
print("\n========== DUPLICATE RECORDS ==========")
print(df[df.duplicated()])

# 7. Count duplicate records
print("\n========== NUMBER OF DUPLICATES ==========")
print(df.duplicated().sum())

# 8. Remove duplicate records
df = df.drop_duplicates()

print("\n========== AFTER REMOVING DUPLICATES ==========")
print(df)

# 9. Handle missing values

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing Attendance with mean
df["Attendance"] = df["Attendance"].fillna(
    df["Attendance"].mean()
)

# 10. Check missing values after cleaning
print("\n========== MISSING VALUES AFTER CLEANING ==========")
print(df.isnull().sum())

# 11. Find shape of cleaned dataset
print("\n========== CLEANED DATASET SHAPE ==========")
print(df.shape)

# 12. Display final cleaned dataset
print("\n========== FINAL CLEANED DATASET ==========")
print(df)

# 13. Save cleaned dataset
df.to_csv("Day7/task1/cleaned_students.csv", index=False)

print("\n========== SUCCESS ==========")
print("Cleaned dataset saved successfully!")