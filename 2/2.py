print('\n-------------------------------------------\n')
print('                   DAY 2')
print('\n-------------------------------------------\n')

# Open and load data
with open('input.txt', 'r') as open_file:
    input_data = open_file.readlines()

##############################################################################

print('\n===================  PART 1  ======================\n')

# Convert to list of tuples
data = [ (row.split(' ')[0], int(row.split(' ')[1])) for row in input_data ]

horizontal, depth = 0, 0
for index, move in enumerate(data):
    direction = move[0]
    amount = move[1]
    if direction == "forward":
        horizontal += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount
print(f'Steps: {index + 1} - Horizontal: {horizontal} - Depth: {depth} - Product: {horizontal * depth}')

print('\n===================  PART 2  ======================\n')

horizontal, depth, aim = 0, 0, 0
for index, move in enumerate(data):
    direction = move[0]
    amount = move[1]
    if direction == "forward":
        horizontal += amount
        depth += aim * amount
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount
print(f'Steps: {index + 1} - Horizontal: {horizontal} - Depth: {depth} - Aim: {aim} - Product: {horizontal * depth}')
