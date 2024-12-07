import re

with open("Day3/input.txt") as file:
    lines = file.readlines()

total = 0

for line in lines:

    x = re.findall("mul\(\d{1,3}\,\d{1,3}\)", line)
    

    for equation in x:
        numbers = equation[4:-1].split(",")
        multiply = int(numbers[0])*int(numbers[1])
        print(multiply)
        total += multiply

print(total)