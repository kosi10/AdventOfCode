with open("Day3/input.txt") as file:
    lines = file.readlines()

#print(lines[0].find("mul"))
print(lines[0].count("mul"))

strBuilder = ""
i = 0

for letter in lines[0]:
    if letter == "m" and strBuilder == "":
        strBuilder += letter
        print("m")
        continue
    elif letter == "u" and strBuilder == "m":
        print("u")
        strBuilder += letter
    elif letter == "l" and strBuilder == "mu":
        print("l")
        strBuilder += letter
    elif letter == "(" and strBuilder == "mul":
        strBuilder += letter
    elif letter.isdigit() and strBuilder == "mul(":
        strBuilder += letter
        print("digits")


a = "1"
print(type(a))
print(a.isdigit())