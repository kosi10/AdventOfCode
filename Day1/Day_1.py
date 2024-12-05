with open("arrays.txt") as file:
    lines = [line.rstrip() for line in file]

arr1 = []
arr2 = []

for line in lines:
    x = line.split()
    arr1.append(x[0])
    arr2.append(x[1])

razlikaKoncna = 0

for i in range (len(lines)):
    min1 = min(arr1)
    min2 = min(arr2)
    arr1.remove(min1)
    arr2.remove(min2)
    razlika = abs(int(min1) - int(min2))
    razlikaKoncna += razlika

print(razlikaKoncna)