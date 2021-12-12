print('\n-------------------------------------------\n')
print('                   DAY 1')
print('\n-------------------------------------------\n')

# Open and load data
with open('input.txt', 'r') as open_file:
    input_data = open_file.readlines()

##############################################################################

print('\n===================  PART 1  ======================\n')
# Convert to integer and add to list
data = [ int(row) for row in input_data ]

increased = 0
for index, current_item in enumerate(data):
    if index > 0:
        previous_item = data[index - 1]
        if previous_item - current_item < 0:
            increased += 1
        # print(f'{index}: {previous_item} - {current_item} - {previous_item - current_item < 0} - {increased}')
print(f'Increased: {increased} of {len(data)}')

print('\n===================  PART 2  ======================\n')
sum_of_three = []
increased = 0
for index, current_item in enumerate(data):
    if index > 1:
        sum_of_three.append(data[index] + data[index - 1] + data[index - 2])

for index, current_item in enumerate(sum_of_three):
    if index > 0:
        previous_item = sum_of_three[index - 1]
        if previous_item - current_item < 0:
            increased += 1
        # print(f'{index}: {previous_item} - {current_item} - {previous_item - current_item < 0} - {increased}')
print(f'Increased: {increased} of {len(data)}')



