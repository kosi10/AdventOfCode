import re

with open("Day3/input.txt") as file:
    lines = file.readlines()

total = 0
newString = ""

arr = []

for line in lines:

    split = re.split("do\(\)", line)
    print(len(split))

    for el in split:

        #split2 = re.split("don\'t\(\)", el)
        #arr.append(split2[0])
        
    break

'''
for lin in arr:
    x = re.findall("mul\(\d{1,3}\,\d{1,3}\)", lin)

    for equation in x:
        numbers = equation[4:-1].split(",")
        multiply = int(numbers[0])*int(numbers[1])
        total += multiply

print(total)
'''