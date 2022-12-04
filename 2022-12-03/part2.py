with open("input.txt") as input_file:
    input_values = input_file.read().splitlines()


def divide_chunks(l):
    for i in range(0, len(l), 3):
        yield l[i : i + 3]


groups = list(divide_chunks(input_values))

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
characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

for letter in same_chars_all:
    value = characters.index(letter) + 1
    total_val += value

print(total_val)
