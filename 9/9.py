print("\n-------------------------------------------\n")
print("                   DAY 9")
print("\n-------------------------------------------\n")

from pprint import pprint
import math

# Open and load data
with open("sample.txt", "r") as open_file:
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

def scan_adjacent(row: int, col: int, data: list, basin_index: int) -> None:
    try:
        middle = int(data[row][col])
    except:
        print("  STOP - Edge hit")
        return

    print("")
    print(f"....... {middle} {row, col} .........")

    up_grad = abs(int(data[row - 1][col]) - middle) if row > 0 else 9999
    down_grad = abs(int(data[row + 1][col]) - middle) if row < len(data) - 1 else 9999
    left_grad = abs(int(data[row][col - 1]) - middle) if col > 0 else 0
    right_grad = (abs(int(data[row][col + 1]) - middle) if col < len(data[row]) - 1 else 9999)

    print(f"Up: {up_grad} | Down: {down_grad} | Left: {left_grad} | Right: {right_grad}")

    if (
        up_grad == 1
        and (row - 1, col) not in basins[basin_index]
        and int(data[row - 1][col]) != 9
    ):
        print(f"  Step UP to {row - 1, col}")
        basins[basin_index].append((row - 1, col))
        scan_adjacent(row - 1, col, data, basin_index)

    if (
        down_grad == 1
        and (row + 1, col) not in basins[basin_index]
        and int(data[row + 1][col]) != 9
    ):
        print(f"  Step DOWN to {row + 1, col}")
        basins[basin_index].append((row + 1, col))
        scan_adjacent(row + 1, col, data, basin_index)

    if (
        left_grad == 1
        and (row, col - 1) not in basins[basin_index]
        and int(data[row][col - 1]) != 9
    ):
        print(f"  Step LEFT to {row, col - 1}")
        basins[basin_index].append((row, col - 1))
        scan_adjacent(row, col - 1, data, basin_index)

    if (
        right_grad == 1
        and (row, col + 1) not in basins[basin_index]
        and int(data[row][col + 1]) != 9
    ):
        print(f"  Step RIGHT to {row, col + 1}")
        basins[basin_index].append((row, col + 1))
        scan_adjacent(row, col + 1, data, basin_index)

    return


for basin_index, (row_low_point, col_low_point) in enumerate(low_point_coordinates):
    low_point = data[row_low_point][col_low_point]

    print("\n")
    print(f"========= BASIN: {basin_index} - LP: {low_point} {row_low_point, col_low_point} ===========")

    basins.append([(row_low_point, col_low_point)])
    scan_adjacent(
        row_low_point,
        col_low_point,
        data,
        basin_index
    )

print("\n\n")
for basin_index, basin in enumerate(basins):
    print("")
    print(f"Basin Number:    {basin_index + 1}")
    print(f"Basin Location Count: {len(basin)}")
    print(f"Basin Locations: {basin}")

# Product of three largest basins
basin_location_count = [ len(basin) for basin in basins ]
basin_location_count.sort(reverse=True)
print(basin_location_count)
top_basins_total = math.prod(basin_location_count[0:3])

print(f'Product of top three basin sizes: {top_basins_total}')

# 260400