with open("input.txt") as input_file:
    input_values = input_file.read()

elves = input_values.replace("\n",",").split(",,")[:-1]

totals = []
for elf in elves:
    elf = elf.split(",")
    total = 0
    for snack in elf:
        total += int(snack)
    totals.append(total)

totals.sort()

# Most
print(totals[-1])

# Most top three 
total_top_three = 0
for pos in totals[-3:]:
    total_top_three += pos
print(total_top_three)
