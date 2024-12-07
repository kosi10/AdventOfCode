import re

with open("Day4/input.txt") as file:
    lines = file.readlines()
#every lines input has a space at the end

totalCount = 0
tempCount = 0

# check every possible line, backwards and forwards, start with left-right

#check left and right
for line in lines:
    x = re.findall("XMAS", line)
    y = re.findall("XMAS", line[::-1])
    tempCount += (len(x) + len(y))
print(tempCount)
totalCount += tempCount
tempCount = 0


#check up and down
newStrings = [""] * 141

for line in lines:
    counter = 0
    for c in line:
        newStrings[counter] += c
        counter += 1

for line in newStrings[:-1]:
    x = re.findall("XMAS", line)
    y = re.findall("XMAS", line[::-1])
    tempCount += (len(x) + len(y))
print(tempCount)
totalCount += tempCount
tempCount = 0


#check upleft and downright

#i can do this by using both my strings and checking by 2 triangles.