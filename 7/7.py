import csv


print('\n-------------------------------------------\n')
print('                   DAY 7')
print('\n-------------------------------------------\n')

# Open and load data
with open('input.csv', 'r') as open_file:
    myreader = csv.reader(open_file)
    input_data = [ row for row in myreader ][0]
    input_data = [ int(item) for item in input_data ]

##############################################################################

print('\n===================  PART 1  ======================\n')

align_and_fuel = []
for index, align_pos in enumerate(input_data):
    total_fuel = 0
    for crab_position in input_data:
        crab_movement = abs(crab_position - align_pos)
        total_fuel += crab_movement
    align_and_fuel.append((align_pos, total_fuel))

cheapest = min(align_and_fuel, key = lambda t: t[1])
print(f'Cheapest Align Position: {cheapest[0]}')
print(f'Cheapest Total Fuel    : {cheapest[1]}')


print('\n===================  PART 2  ======================\n')

align_and_fuel = []
for index, align_pos in enumerate(input_data):
    total_fuel = 0
    for crab_position in input_data:
        crab_movement = abs(crab_position - align_pos)
        crab_fuel = sum([ step for step in range(1, crab_movement + 1) ])
        total_fuel += crab_fuel
    align_and_fuel.append((align_pos, total_fuel))

cheapest = min(align_and_fuel, key = lambda t: t[1])
print(f'Cheapest Align Position: {cheapest[0]}')
print(f'Cheapest Total Fuel    : {cheapest[1]}')
