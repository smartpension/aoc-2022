import sys
with open("input.txt") as input_file:
    input_values = str(input_file.read().splitlines())

input_values = ''.join(filter(str.isalpha, input_values))

for length in [4,14]:
    buffer = []
    for index,letter in enumerate(input_values):
        if len(buffer) == length:
            del buffer[0]
        buffer.append(letter)
        if len(set(buffer)) > (length -1):
            print(index +1)
            break
