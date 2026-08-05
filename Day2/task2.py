x = []

while True:
    numbers = input("Enter numbers: ")

    if numbers == "done":
        break

    x.append(int(numbers))

print("Minimum number is:", min(x))
print("Maximum number is:", max(x))
print("Sum of numbers is:", sum(x))
print("Average of numbers is:", sum(x) / len(x))
print("Total length of numbers is:", len(x))
print("Sorted numbers are:", sorted(x))