import pandas as pd
names = pd.Series(["Alice", "BOB", None, "Charlie", "DAVID", None, "Eve"])
print("Original Series:\n",names)

print("\nMissing values:\n",names.isna())
names = names.fillna("Unknown")
print("\nAfter filling missing values:")
print(names)

names = names.str.lower()
print("\nNames in lowercase:")
print(names)
filtered_names = names[names.str.contains("a")]
print("\nNames containing the letter 'a':")
print(filtered_names)