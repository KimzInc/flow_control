# numbers = "9,223;372:036 854,775;807"
numbers = input("Please enter a series of numbers, using any separators you like: ")
# separators = numbers[1::4]
num = []
separators = ""
for char in numbers:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in numbers).split()
# print([int(val) for val in values])
print(sum([int(val) for val in values]))
