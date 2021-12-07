print('\n-------------------------------------------\n')
print('                   DAY 1')
print('\n-------------------------------------------\n')


# Open and load data
with open('data.txt', 'r') as open_file:
    rows = open_file.readlines()

# Convert to integer and add to list
data = [ int(row) for row in rows ]

##############################################################################

increased = 0
for index, current_item in enumerate(data):
    if index > 0:
        previous_item = data[index - 1]
        if previous_item - current_item < 0:
            increased += 1
        print(f'{index}: {previous_item} - {current_item} - {previous_item - current_item < 0} - {increased}')
print(f'Increased: {increased} of {len(data)}')


##############################################################################
print('\n-------------------------------------------\n')


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
        print(f'{index}: {previous_item} - {current_item} - {previous_item - current_item < 0} - {increased}')
print(f'Increased: {increased} of {len(data)}')



