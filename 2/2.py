print('\n-------------------------------------------\n')
print('                   DAY 2')
print('\n-------------------------------------------\n')

# Open and load data
with open('data.txt', 'r') as open_file:
    rows = open_file.readlines()

##############################################################################

print('\n===================  PART 1  ======================\n')
# NOTE:
# forward X increases the horizontal position by X units.
# down X increases the depth by X units. (depth increases)
# up X decreases the depth by X units. (depth decreases)

# Convert to list of tuples
data = [ (row.split(' ')[0], int(row.split(' ')[1])) for row in rows ]

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
# NOTE:
# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#     It increases your horizontal position by X units.
#     It increases your depth by your aim multiplied by X.

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
