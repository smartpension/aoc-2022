with open("input.txt") as input_file:
    input_values = input_file.readlines()

same_chars_all = []

for backpack in input_values:
    same_chars = []
    left = slice(0, len(backpack) // 2)
    right = slice(len(backpack) // 2, len(backpack))
    for item in backpack[left]:
        if item in backpack[right]:
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
