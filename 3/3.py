print('\n-------------------------------------------\n')
print('                   DAY 3')
print('\n-------------------------------------------\n')


# Open and load data
with open('data.txt', 'r') as open_file:
    rows = open_file.readlines()
data = [ (row.strip('\n')) for row in rows ]

##############################################################################

print('\n===================  PART 1  ======================\n')

columns = []
for bit_index in range(len(data[0])):
    column = []
    for row in data:
        column.append(row[bit_index])
    columns.append(''.join(column))

gamma_rate = ''
epsilon_rate = ''
for column in columns:
    if column.count('0') > column.count('1'):
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

gamma_rate_int = int(gamma_rate, 2)
epsilon_rate_int = int(epsilon_rate, 2)
submarine_power = gamma_rate_int * epsilon_rate_int

print(f'Gamma Rate  :                {gamma_rate_int}')
print(f'Epsilon Rate:                {epsilon_rate_int}')
print(f'Submarine Power consumption: {submarine_power}')


print('\n===================  PART 2  ======================\n')

from copy import deepcopy

def find_rating(rating_type: str) -> int:
    """Finding Oxygen Generator or CO2 Scrubber Rating"""
    data_copy = deepcopy(data)
    for bit_index in range(len(data[0])):
        column = []
        for row in data_copy:
            column.append(row[bit_index])

        item_1 = column.count('0')
        item_2 = column.count('1')
        if rating_type == 'oxygen':
            pass
        elif rating_type == 'co2':
            item_1, item_2 = item_2, item_1

        if item_1 > item_2:
            data_copy = [row for row in data_copy if row[bit_index] == '0']
        elif item_1 == item_2:
            keep_bit = '1' if rating_type == 'oxygen' else '0'
            data_copy = [row for row in data_copy if row[bit_index] == keep_bit]
        else:
            data_copy = [row for row in data_copy if row[bit_index] == '1']

        if len(data_copy) == 1:
            break

    return int(data_copy[0], 2)

oxygen_generator_rating = find_rating(rating_type="oxygen")
co2_scrubber_rating = find_rating(rating_type="co2")

print(f'Oxygen Generator Rating: {oxygen_generator_rating}')
print(f'CO2 Scrubber Rating:     {co2_scrubber_rating}')
print(f'Life support rating:     {oxygen_generator_rating * co2_scrubber_rating}')
