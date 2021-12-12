print("\n-------------------------------------------\n")
print("                   DAY 11")
print("\n-------------------------------------------\n")

from pprint import pprint
from copy import deepcopy
import sys

# Open and load data
with open("data.txt", "r") as open_file:
    rows = open_file.readlines()
data = [(row.strip("\n")) for row in rows]

# Convert all to integers
data_orig = [ [ int(octo) for octo in row ] for row in data ]

##############################################################################

print("\n===================  PART 1  ======================\n")

data = deepcopy(data_orig)

def check_flash(row_index: int, col_index: int) -> None:
    global total_flashed
    if (row_index, col_index) in flashed:
        return

    data[row_index][col_index] += 1  # Increase the energy level

    if data[row_index][col_index] > 9:  # Check if octo has flashed
        total_flashed += 1
        flashed.append((row_index, col_index))
        data[row_index][col_index] = 0

        # Check adjacent
        for x in [-1, 0, 1]:  # Check adjacent along horizontal
            if row_index + x < 0 or row_index + x > 9:
                continue
            for y in [-1, 0, 1]:  # Check adjacent along vertical
                if col_index + y < 0 or col_index + y > 9:
                    continue
                check_flash(row_index + x, col_index + y)

number_of_steps = 100
total_flashed = 0
for step in range(number_of_steps):
    flashed = []
    for row_index, row in enumerate(data):
        for col_index, _ in enumerate(row):
            check_flash(row_index, col_index)

print(f'Final dumbo octopus energy levels after {number_of_steps} steps:')
pprint(data)
print(f'Total octopuses that flashed after {number_of_steps}: {total_flashed}')


print("\n===================  PART 2  ======================\n")

data = deepcopy(data_orig)
number_of_steps = 10000
for step in range(number_of_steps):
    flashed = []
    for row_index, row in enumerate(data):
        for col_index, _ in enumerate(row):
            check_flash(row_index, col_index)

    if sum([ sum(row) for row in data ]) == 0:
        break

print(f'First step all octopuses flash: {step + 1}')