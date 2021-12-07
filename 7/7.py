print('\n-------------------------------------------\n')
print('                   DAY 7')
print('\n-------------------------------------------\n')

import csv

with open('data.csv', 'r') as open_file:
    myreader = csv.reader(open_file)
    data = [ row for row in myreader ][0]
    data = [ int(item) for item in data ]

##############################################################################

print('\n===================  PART 1  ======================\n')

crab_positions = data
align_and_fuel = []
for index, align_pos in enumerate(crab_positions):
    total_fuel = 0
    for crab_position in crab_positions:
        crab_movement = abs(crab_position - align_pos)
        total_fuel += crab_movement
    align_and_fuel.append((align_pos, total_fuel))
    # print(f'Align Position: {align_pos} - Total Fuel: {total_fuel}')

cheapest = min(align_and_fuel, key = lambda t: t[1])
print(f'Cheapest Align Position: {cheapest[0]}')
print(f'Cheapest Total Fuel    : {cheapest[1]}')


print('\n===================  PART 2  ======================\n')

# NOTE:
# The first step costs 1,
# the second step costs 2,
# the third step costs 3, and so on.

crab_positions = data
align_and_fuel = []
for index, align_pos in enumerate(crab_positions):
    total_fuel = 0
    for crab_position in crab_positions:
        crab_movement = abs(crab_position - align_pos)
        crab_fuel = sum([ step for step in range(1, crab_movement + 1) ])
        total_fuel += crab_fuel
    align_and_fuel.append((align_pos, total_fuel))
    # print(f'Align Position: {align_pos} - Total Fuel: {total_fuel}')

cheapest = min(align_and_fuel, key = lambda t: t[1])
print(f'Cheapest Align Position: {cheapest[0]}')
print(f'Cheapest Total Fuel    : {cheapest[1]}')
