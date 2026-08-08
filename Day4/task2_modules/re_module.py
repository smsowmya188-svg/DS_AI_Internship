import re

text = "I have 10 apples and 20 oranges."

numbers = re.findall("[0-9]+", text)

print(numbers)