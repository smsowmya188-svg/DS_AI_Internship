# ============================================
# COMPLETE EDA - TITANIC DATASET
# ============================================

# 1. Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================
# 2. Load Dataset
# ============================================

df = sns.load_dataset("titanic")

print("First 5 Rows:")
print(df.head())


# ============================================
# 3. Basic Information
# ============================================

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Information:")
df.info()


# ============================================
# 4. Statistical Summary
# ============================================

print("\nStatistical Summary:")
print(df.describe())


# ============================================
# 5. Missing Values
# ============================================

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================
# 6. Data Cleaning
# ============================================

# Remove deck column because it has many missing values
df = df.drop("deck", axis=1)

# Fill missing Age with median
df["age"] = df["age"].fillna(df["age"].median())

# Fill missing Embarked with mode
df["embarked"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)

# Fill missing Embark Town with mode
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================
# 7. CREATE AGE GROUP
# ============================================

# Create age groups using integer values
# 1 = Child
# 2 = Teenager
# 3 = Adult
# 4 = Middle Age
# 5 = Senior

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=[1, 2, 3, 4, 5]
)

# Convert age_group to integer
df["age_group"] = df["age_group"].astype(int)

print("\nAge Group:")
print(df[["age", "age_group"]].head(10))

print("\nAge Group Data Type:")
print(df["age_group"].dtype)


# ============================================
# 8. UNIVARIATE ANALYSIS
# ============================================

# Age Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df["age"], kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# Fare Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df["fare"], kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()


# Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="sex", data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


# Passenger Class Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="class", data=df)
plt.title("Passenger Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()


# Age Group Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="age_group", data=df)
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()


# ============================================
# 9. BIVARIATE ANALYSIS
# ============================================

# Gender vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(
    x="sex",
    hue="survived",
    data=df
)
plt.title("Gender vs Survival")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


# Class vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(
    x="class",
    hue="survived",
    data=df
)
plt.title("Passenger Class vs Survival")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()


# Age vs Survival
plt.figure(figsize=(6, 4))
sns.boxplot(
    x="survived",
    y="age",
    data=df
)
plt.title("Age vs Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()


# Fare vs Survival
plt.figure(figsize=(6, 4))
sns.boxplot(
    x="survived",
    y="fare",
    data=df
)
plt.title("Fare vs Survival")
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.show()


# Age Group vs Survival
plt.figure(figsize=(6, 4))
sns.countplot(
    x="age_group",
    hue="survived",
    data=df
)
plt.title("Age Group vs Survival")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()


# ============================================
# 10. SKEWNESS ANALYSIS
# ============================================

print("\n========== SKEWNESS ==========")

print(
    df[
        ["age", "fare", "sibsp", "parch", "age_group"]
    ].skew()
)


# ============================================
# 11. CORRELATION ANALYSIS
# ============================================

print("\n========== CORRELATION ==========")

correlation = df[
    ["survived", "age", "fare", "sibsp", "parch", "age_group"]
].corr()

print(correlation)


# Correlation Heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()


# ============================================
# 12. OUTLIER DETECTION
# ============================================

# Age Outliers
plt.figure(figsize=(6, 4))

sns.boxplot(
    x=df["age"]
)

plt.title("Age Outliers")
plt.xlabel("Age")
plt.show()


# Fare Outliers
plt.figure(figsize=(6, 4))

sns.boxplot(
    x=df["fare"]
)

plt.title("Fare Outliers")
plt.xlabel("Fare")
plt.show()


# ============================================
# 13. PATTERN IDENTIFICATION
# ============================================

print("\n========== PATTERN IDENTIFICATION ==========")


# Survival by Gender
print("\nSurvival Rate by Gender:")
print(
    df.groupby("sex")["survived"].mean()
)


# Survival by Class
print("\nSurvival Rate by Class:")
print(
    df.groupby("class")["survived"].mean()
)


# Average Fare by Class
print("\nAverage Fare by Class:")
print(
    df.groupby("class")["fare"].mean()
)


# Survival by Age Group
print("\nSurvival Rate by Age Group:")
print(
    df.groupby("age_group")["survived"].mean()
)


# ============================================
# 14. FINAL DATASET
# ============================================

print("\n========== FINAL DATASET ==========")

print(df.head())

print("\nFinal Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)


# ============================================
# 15. FINAL INSIGHTS
# ============================================

print("\n========== FINAL INSIGHTS ==========")

print("""
1. The Titanic dataset contains numerical and categorical data.

2. Missing values were identified and handled.

3. Age was filled using the median value.

4. Embarked and Embark Town missing values were filled using
   their mode values.

5. The deck column was removed because it contained many
   missing values.

6. Age Group was created using integer values:
      1 = Child
      2 = Teenager
      3 = Adult
      4 = Middle Age
      5 = Senior

7. Female passengers generally had a higher survival rate
   than male passengers.

8. First-class passengers generally had a higher survival
   rate than second- and third-class passengers.

9. Fare is positively skewed because some passengers paid
   very high fares.

10. High fare values were detected as potential outliers.

11. Passenger class and fare show a relationship.

12. Age Group can be used as a numerical feature for
    further analysis or machine learning.

EDA COMPLETED SUCCESSFULLY!
""")