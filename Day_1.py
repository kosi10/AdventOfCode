with open("arrays.txt") as file:
    lines = [line.rstrip() for line in file]

arr1 = []
arr2 = []

for line in lines:
    x = line.split()
    arr1.append(x[0])
    arr2.append(x[1])

razlike = []

for i in range (len(lines)):
    min1 = min(arr1)
    min2 = min(arr2)
    arr1.remove(min1)
    arr2.remove(min2)

    razlika = int(min2)-int(min1)
    razlike.append(abs(razlika))
print(razlike)


