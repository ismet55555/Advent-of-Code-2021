from pprint import pprint
from copy import deepcopy


print("\n-------------------------------------------\n")
print("                   DAY 4")
print("\n-------------------------------------------\n")

# Open and load data
with open("sample.txt", "r") as open_file:
    rows = open_file.readlines()
input_data = [(row.strip("\n")) for row in rows]

##############################################################################

print("\n===================  PART 1  ======================\n")

# Load the input draw numbers
draw_numbers = [ int(draw_number) for draw_number in input_data[0].split(',') ]

# Remove input numbers
input_data = input_data[2::]

def load_boards() -> list:
    boards = [[]]
    boards_marks = [[]]

    # Load the bingo boards
    board_index = 0
    for row in input_data:
        if row:
            # Convert row to integer and add to board
            row_int = [ int(char) for char in row.split(' ') if char ]
            boards[board_index].append(row_int)

            # Create blank board for marks
            zeros = [0]*len(row_int)
            boards_marks[board_index].append(zeros)
        else:
            boards.append([])
            boards_marks.append([])
            board_index += 1

    return boards, boards_marks

boards, boards_marks = load_boards()
winning_board = None

for draw_number in draw_numbers:
    print(f'\n\n=============  Draw Number: {draw_number}  ===============')

    for board_index, board in enumerate(boards):
        print(f'\n=========== Board: {board_index} ===========')
        pprint(board)

        # Add the mark to the board
        for row_index, row in enumerate(board):
            for col_index, number in enumerate(row):
                if number == draw_number:
                    boards_marks[board_index][row_index][col_index] = 1
        pprint(boards_marks[board_index])

        # Check if the board won - horizontal
        for row_index, row in enumerate(boards_marks[board_index]):
            if sum(row) == 5:
                winning_board = board_index
                winning_sequence = row
                print("WON !!!! (HORIZONTAL)")
                break

        # Check if board won - vertical
        for index in range(5):
            col = [ row[index] for row in boards_marks[board_index] ]
            if sum(col) == 5:
                print("WON !!!! (VERTICAL)")
                winning_board = board_index
                winning_sequence = col
                break

        # Check if board won - diagonal
        # TODO

        if winning_board:
            break
    
    if winning_board:
        break


# TODO




