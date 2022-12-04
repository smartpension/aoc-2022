with open("input.txt") as input_file:
    input_values = input_file.read()

elves = input_values.replace("\n", ",").split(",,")[:-1]

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

# Combined top 3
print(sum(totals[-3:]))
