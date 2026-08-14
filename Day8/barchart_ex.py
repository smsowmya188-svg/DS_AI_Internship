import matplotlib.pyplot as plt

students = ["Amit", "Rahul", "Priya", "Sneha", "Kiran"]
marks = [75, 82, 68, 90, 78]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()