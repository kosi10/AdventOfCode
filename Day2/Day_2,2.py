with open("Day2/arrays.txt") as file:
    lines = [line.rstrip() for line in file]

# 1 = increasing, 0 = decreasing
constant = -1
unsafe = 0
counter = 0
a = 0

#goes through all lines
for line in lines:
    x = line.split()
    
    
    print(len(x))
    #goes through but deleting a element each time
    for i in range(len(x)):
        a = True
        last = -1

        # goes through each value in a line
        saved = x[i]

        x.pop(i)
        #print(x)
        
        for num in x:

            #first goes through
            if last == -1:
                last = int(num)

            else: # < for decreasing, > increasing
                if int(num) < int(last) and abs(int(num) - int(last)) < 4: 
                    print(num,last)
                    last = int(num)
                    continue
                else:
                    a = False
                    break
            last = int(num)
        if a == True:
            counter+=1
            break
        x.insert(i,saved)