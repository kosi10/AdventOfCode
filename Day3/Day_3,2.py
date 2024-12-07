import re

with open("Day3/input.txt") as file:
    lines = file.readlines()

total = 0
newString = ""
arr = []

#This part is important
for line in lines:
    newString+= line

#splits the string after every do() so every new string starts as enabled
split = re.split("do\(\)", newString)

#there are no additional "do()" in the string so the string is enabled until the first "don't" is found
for el in split:

    split2 = re.split("don\'t\(\)", el)
    arr.append(split2[0])

# find the mul(x,y) sequence with regex
for lin in arr:
    x = re.findall("mul\(\d{1,3}\,\d{1,3}\)", lin)

    for equation in x:
        numbers = equation[4:-1].split(",")
        multiply = int(numbers[0])*int(numbers[1])
        total += multiply

print(total)
