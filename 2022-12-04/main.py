with open("input.txt") as input_file:
    input_values = input_file.read().splitlines()

count = 0
any_count = 0

for pair in input_values:
    first = pair.split(",")[0]
    second = pair.split(",")[1]

    first_list = range(int(first.split("-")[0]), int(first.split("-")[1]) + 1)
    second_list = range(int(second.split("-")[0]), int(second.split("-")[1]) + 1)

    if all(item in first_list for item in second_list):
        count += 1
    elif all(item in second_list for item in first_list):
        count += 1

    if any(item in first_list for item in second_list):
        any_count += 1

print(count)
print(any_count)

