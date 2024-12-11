with open("Day5/input.txt") as file:
    lines = file.readlines()

# in this function i get incorrect updates and i need to fix them, to help me start i have the leading number where it got wrong
def fix(line,lead, problem):
    counter = 0
    for num in line:
        if(num == lead):
            break
        counter += 1
    
    for num in line[counter:]:
        print(counter)


    print(line,lead,problem)
    exit()


# rules has rules, updates are ints in an array 
rules = []
updates = []

for line in lines: 
    if line == "\n":
        continue
    if line[2] == '|':
        rules.append(line[:-1])
    else:
        updates.append(line[:-1])


# lead tells me what numbers are after a key and follow what numbers are in front of the key
lead = {}
follow = {}

for rule in rules:
    #makes it to a simple list of 2
    nums = list(map(int, rule.split('|')))

    # makes 2 dictionaries lead has unique keys from 1.st column, follow from second. added values from the other column
    if nums[0] in lead:
        lead[nums[0]].add(nums[1])
    else:
        lead[nums[0]] = {nums[1]}

    if nums[1] in follow:
        follow[nums[1]].add(nums[0])
    else:
        follow[nums[1]] = {nums[0]}

correct = []
found = False


for update in updates:
    counter = 0 
    update = list(map(int, update.split(",")))
    # for every number in sequence check if all the ones who follow it are correct
    for num in update[:-1]:
        counter += 1
        found = False
        # check every number if it follows our leading number as per the rules
        for test in update[counter:]:
            if test in lead[num]:
                found = True
            else:
                found = False
                break      
        if(found == False):
           fix(update, num, test)
           break
    if(found):
        correct.append(update)

totalSum = 0
# in correct_final if double checking
for line in correct:
    index = len(line) // 2
    totalSum += line[index]
print(totalSum)