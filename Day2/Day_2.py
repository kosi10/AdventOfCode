with open("Day2/arrays.txt") as file:
    lines = [line.rstrip() for line in file]

# 1 = increasing, 0 = decreasing
constant = -1
unsafe = 0
counter = 0
a = 0
arr1 = []

#goes through all lines
for line in lines:
    x = line.split()
    last = -1
    a = True
    first = 0

    # goes through each value in a line
    for num in x:

        #first goes through
        if last == -1:
            last = int(num)

        else: # < za vse padajoce, > rastoce
            if int(num) > int(last) and abs(int(num) - int(last)) < 4: 
                print(num,last)
                last = int(num)
                continue
            else:
                #print("ni res")
                a = False
                break
        last = int(num)
    if a == True:
        counter+=1
        if(first == 1):
            arr1.append(x)
        
print(counter)
print(arr1)