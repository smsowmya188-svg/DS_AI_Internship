import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Rahul", 85])
    writer.writerow(["Anita", 90])
    writer.writerow(["Kiran", 78])

print("CSV file created")