with open("input.txt") as input_file:
    input_values = input_file.read().splitlines()

groups = []

for i in range(0, len(input_values), 3):
    groups.append(input_values[i : i + 3])

same_chars_all = []

for group in groups:
    same_chars = []
    for item in group[0]:
        if item in group[1] and item in group[2]:
            same_chars.append(item)
    same_chars = list(set(same_chars))
    for char in same_chars:
        same_chars_all.append(char)

total_val = 0
characters = list(map(chr, range(ord("a"), ord("z") + 1))) + list(
    map(chr, range(ord("A"), ord("Z") + 1))
)

for letter in same_chars_all:
    value = characters.index(letter) + 1
    total_val += value

print(total_val)
