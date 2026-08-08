from itertools import combinations

items = ["A", "B", "C"]

result = combinations(items, 2)

for item in result:
    print(item)