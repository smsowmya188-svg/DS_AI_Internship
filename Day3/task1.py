def result(name, marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    elif avg >= 50:
        grade = "E"
    else:
        grade = "Fail"

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Average:", avg)
    print("Grade:", grade)

name = input("Enter Student Name: ")
marks = []

while True:
    m = input("Enter Mark (or done): ")

    if m == "done":
        break

    marks.append(int(m))

result(name, marks)