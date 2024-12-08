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

upLeftDiagonal1 = [""] * 279
shift = 0
for line in lines:
    counter = 0
    #last line has no space at the end
    if shift == 139:
        for c in line:
            upLeftDiagonal1[counter + shift] += c
            counter += 1
        break
    for c in (line[:-1]):
        upLeftDiagonal1[counter + shift] += c
        counter += 1
    shift += 1

# ze za inverted 
upLeftDiagonal2 = [""] * 279
shift = 0
for line in lines:
    counter = 0
    #last line has no space at the end
    if shift == 139:
        for c in line[::-1]:
            upLeftDiagonal2[counter + shift] += c
            counter += 1
        break
    for c in (line[:-1])[::-1]:
        upLeftDiagonal2[counter + shift] += c
        counter += 1
    shift += 1

#check left and right for new arrays
for line in upLeftDiagonal1:
    x = re.findall("XMAS", line)
    y = re.findall("XMAS", line[::-1])
    tempCount += (len(x) + len(y))

totalCount += tempCount
tempCount = 0

for line in upLeftDiagonal2:
    x = re.findall("XMAS", line)
    y = re.findall("XMAS", line[::-1])
    tempCount += (len(x) + len(y))
totalCount += tempCount

print(totalCount)