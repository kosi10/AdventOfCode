with open("Day1/arrays.txt") as file:
    lines = [line.rstrip() for line in file]

arr1 = []
arr2 = []

for line in lines:
    x = line.split()
    arr1.append(x[0])
    arr2.append(x[1])

sum = 0

for val1 in arr1:
    print(val1)
    similarity = 0
    counter = 0
    for val2 in arr2:
        if val1 == val2:
            counter+=1
    similarity = int(val1) *counter
    sum += similarity

print(sum)