with open("Day5/input.txt") as file:
    lines = file.readlines()

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

#print(lead)
#print(follow)
correct = []

for update in updates:
    counter = 0 
    update = list(map(int, update.split(",")))
    for num in update[:-1]:
        counter += 1
        #print(num)
        #print(lead[num])
        found = False
        # v tem foru za vsako cifro preverim ce so vse ki je sledijo kot value v seznamu lead.
        for test in update[counter:]:
            #print(test)
            if test in lead[num]:
                #print(test, "je v mojem seznamu")
                found = True
                break
        if(found == False):
           break
    if(found):
        correct.append(update)


print(len(correct))

#moram preveriti se v obratno smer in drug seznam 
correct_final = []

for update in correct:
    update = update[::-1]
    counter = 0 

    for num in update[:-1]:
        counter += 1
        found = False
        # v tem foru za vsako cifro preverim ce so vse ki je sledijo kot value v seznamu lead.
        for test in update[counter:]:
            #print(test)
            if test in follow[num]:
                #print(test, "je v mojem seznamu")
                found = True
                break
        if(found == False):
           break
    if(found):
        correct_final.append(update)

print(len(correct_final))

totalSum = 0
for line in correct_final:
    index = len(line) // 2
    totalSum += line[index]
print(totalSum)