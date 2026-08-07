def calculate_result(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    elif average >= 35:
        grade = "E"
    else:
        grade = "F"

    return total, average, grade


students = []

while True:
    name = input("Enter student name (or done to stop): ")

    if name.lower() == "done":
        break

    marks = []

    for i in range(5):
        mark = int(input("Enter marks: "))
        marks.append(mark)

    total, average, grade = calculate_result(name, marks)

    students.append([name, total, average, grade])


print("\n----- CLASS RESULTS -----")

for student in students:
    print("Name:", student[0])
    print("Total Marks:", student[1])
    print("Average:", student[2])
    print("Grade:", student[3])
    print("------------------------")