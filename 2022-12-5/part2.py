with open("input.txt") as input_file:
    input_values = input_file.read().splitlines()

block_lines = []

# Build lists
for orig_line in input_values:
    if orig_line == " 1   2   3   4   5   6   7   8   9 ":
        break
    else:
        orig_line = orig_line.replace("    ", " [0] ")
        block_lines.append(orig_line)

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for line in block_lines:
    line = line.split()

    one.insert(0, line[0])
    two.insert(0, line[1])
    three.insert(0, line[2])
    four.insert(0, line[3])
    five.insert(0, line[4])
    six.insert(0, line[5])
    seven.insert(0, line[6])
    eight.insert(0, line[7])
    nine.insert(0, line[8])

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res

all_lists = []
all_lists.append([])
all_lists.append([remove_items(one,"[0]")])
all_lists.append([remove_items(two,"[0]")])
all_lists.append([remove_items(three,"[0]")])
all_lists.append([remove_items(four,"[0]")])
all_lists.append([remove_items(five,"[0]")])
all_lists.append([remove_items(six,"[0]")])
all_lists.append([remove_items(seven,"[0]")])
all_lists.append([remove_items(eight,"[0]")])
all_lists.append([remove_items(nine,"[0]")])

# print(list(dict(all_lists[1]).keys())[0])

for line in input_values:
    if line.startswith("move"):
        move_number = int(line.split()[1])
        source_column = all_lists[int(line.split()[3])]
        destination_column = all_lists[int(line.split()[5])]
        pos = 1
        move_list = []
        while pos <= move_number:
            move_list.append(source_column[0][-1])
            del source_column[0][-1]
            pos += 1
        move_list.reverse()
        destination_column[0] = destination_column[0] + move_list

for column in all_lists:
    print(column)    
