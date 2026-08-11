import pandas as pd
marks = pd.Series([85, 78, 89, 90, 95],index=["Maths", "Science", "English", "Computer",
                                               "Kannada"])
print("Student Marks:")
print(marks)

print("\nMarks at position 0:", marks.iloc[0])
print("Marks at position 1:", marks.iloc[1])
print("Marks at position 2:", marks.iloc[2])

print("\nMarks in Maths:", marks["Maths"])
print("Marks in Computer:", marks["Computer"])

print("\nValues:\n",marks.values)

print("\nIndex:\n",marks.index)

print("\nMarks above 60:\n",marks>60)
