print("\n-------------------------------------------\n")
print("                   DAY 9")
print("\n-------------------------------------------\n")

from pprint import pprint
import math

# Open and load data
with open("data.txt", "r") as open_file:
    rows = open_file.readlines()
data = [(row.strip("\n")) for row in rows]
pprint(data, width=50)


##############################################################################

print("\n===================  PART 1  ======================\n")

risk_level_total = 0
low_point_coordinates = []

for row in range(len(data)):
    for col in range(len(data[row])):
        middle = int(data[row][col])

        up = int(data[row - 1][col]) if row > 0 else 9999
        down = int(data[row + 1][col]) if row < len(data) - 1 else 9999

        left = int(data[row][col - 1]) if col > 0 else 9999
        right = int(data[row][col + 1]) if col < len(data[row]) - 1 else 9999

        adjacent_locations = [up, down, left, right]
        is_middle_low_point = all(
            [middle < location for location in adjacent_locations]
        )
        if is_middle_low_point:
            risk_level_total += middle + 1
            low_point_coordinates.append((row, col))

print(f"Low Point coordinates (row, column): {low_point_coordinates}")
print(f"Risk Level Total: {risk_level_total}")


print("\n===================  PART 2  ======================\n")

basins = []

def scan_location(row: int, col: int, data: list, basin_index: int) -> None:
    try:
        middle = int(data[row][col])
    except:
        print("  STOP - Edge hit")
        return

    print("")
    print(f"....... {middle} {row, col} .........")

    up = abs(int(data[row - 1][col]) - middle) if row > 0 else 9999
    down = abs(int(data[row + 1][col]) - middle) if row < len(data) - 1 else 9999
    left = abs(int(data[row][col - 1]) - middle) if col > 0 else 0
    right = abs(int(data[row][col + 1]) - middle) if col < len(data[row]) - 1 else 9999

    print(f"Up: {up} | Down: {down} | Left: {left} | Right: {right}")

    if (
        up == 1
        and (row - 1, col) not in basins[basin_index]
        and int(data[row - 1][col]) != 9
    ):
        print(f"  Step UP to {row - 1, col} ({data[row - 1][col]})")
        basins[basin_index].append((row - 1, col))
        scan_location(row - 1, col, data, basin_index)

    if (
        down == 1
        and (row + 1, col) not in basins[basin_index]
        and int(data[row + 1][col]) != 9
    ):
        print(f"  Step DOWN to {row + 1, col} ({data[row + 1][col]})")
        basins[basin_index].append((row + 1, col))
        scan_location(row + 1, col, data, basin_index)

    if (
        left == 1
        and (row, col - 1) not in basins[basin_index]
        and int(data[row][col - 1]) != 9
    ):
        print(f"  Step LEFT to {row, col - 1} ({data[row][col - 1]})")
        basins[basin_index].append((row, col - 1))
        scan_location(row, col - 1, data, basin_index)

    if (
        right == 1
        and (row, col + 1) not in basins[basin_index]
        and int(data[row][col + 1]) != 9
    ):
        print(f"  Step RIGHT to {row, col + 1} ({data[row][col + 1]})")
        basins[basin_index].append((row, col + 1))
        scan_location(row, col + 1, data, basin_index)

    print(f"LAST --- Up: {up} | Down: {down} | Left: {left} | Right: {right}")


for basin_index, (row_low_point, col_low_point) in enumerate(low_point_coordinates):
    low_point = data[row_low_point][col_low_point]

    print("\n")
    print(f"========= BASIN: {basin_index} - LP: {low_point} {row_low_point, col_low_point} ===========")

    basins.append([(row_low_point, col_low_point)])
    scan_location(
        row_low_point,
        col_low_point,
        data,
        basin_index
    )

# Sort the basin location areas
[ basin.sort() for basin in basins ]

# Remove duplicate basins
basins_no_duplicates = []
for basin in basins:
    if basin not in basins_no_duplicates:
        basins_no_duplicates.append(basin)

print("\n\n")
for basin_index, basin in enumerate(basins_no_duplicates):
    print(f"----------------  Basin {basin_index + 1}  ----------------")
    print(f"Basin Locations Count: {len(basin)}")
    print(f"Basin Locations      : {basin}")
print('')

# Product of three largest basins
basin_size = [ len(basin) for basin in basins_no_duplicates ]
basin_size.sort(reverse=True)
print(f'Basin sizes: {basin_size}')

top_basins_total = math.prod(basin_size[0:3])
print(f'Product of top three basin sizes: {top_basins_total} ({basin_size[0:3]})')

# Answers Tried:
# 260400   - Too low (70*62*60)
# 15624000 - Too high (70*62*60*60)


##############################################################################
#                                   Plotting
##############################################################################

import numpy as np
import matplotlib.pyplot as plt

print('Plotting ...')

fig = plt.figure()
ax = fig.add_subplot(111)

for basin_index, basin in enumerate(basins_no_duplicates):
    x, y = zip(*basin)
    plt.scatter(y, x, s=20, alpha=0.8)
ax.set_aspect('equal', adjustable='box')

# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(0, 100, 5)
minor_ticks = np.arange(0, 100, 1)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

ax.set_xlim([0, 100])
ax.set_ylim([0, 100])

# And a corresponding grid
ax.grid(which='both')

# Or if you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
plt.show()