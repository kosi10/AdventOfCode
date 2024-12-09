with open("Day4/input.txt") as file:
    lines = file.readlines()

totalCounter = 0

lin1 = lines[0]
lin2 = lines[1]
lin3 = lines[2]

# go throught all lines and look 3 in combination
for line in lines[2:]:
    position = 0
    lin3 = line

    for values in zip(lin1,lin2,lin3):
        if(position > 137):
            break

        topleft = lin1[position]
        topright = lin1[position+2]
        bottomleft = lin3[position]
        bottomright = lin3[position+2]
        middle = lin2[position+1]

        if middle == 'A':
            if topleft == 'M' and bottomright == 'S':
                if topright == 'S' and bottomleft == 'M':
                    totalCounter += 1
                if topright == 'M' and bottomleft == 'S':
                    totalCounter += 1
            if topleft == 'S' and bottomright == 'M':
                if topright == 'S' and bottomleft == 'M':
                    totalCounter += 1
                if topright == 'M' and bottomleft == 'S':
                    totalCounter += 1
        
        position += 1

    lin1 = lin2
    lin2 = lin3
        
print(totalCounter)


# M . S   M . M   S . S   S . M            what i am looking for
# . A .   . A .   . A .   . A .
# M . S   S . S   M . M   S . M
