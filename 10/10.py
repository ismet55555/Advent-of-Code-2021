print("\n-------------------------------------------\n")
print("                   DAY 10")
print("\n-------------------------------------------\n")

# Open and load input_data
with open("input.txt", "r") as open_file:
    rows = open_file.readlines()
input_data = [(row.strip("\n")) for row in rows]

##############################################################################

print("\n===================  PART 1  ======================\n")

syntax_error_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
chunk_pair = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

syntax_error_score = 0
corrupted_row_indexes = []
for row_index, row in enumerate(input_data):
    open_chars = [ row[0] ]
    for index, char in enumerate(row[1:]):
        if char in chunk_pair:
            # Opening character
            open_chars.append(char)
        elif char in chunk_pair.values():
            # Closing character
            if char == chunk_pair[open_chars[-1]]:
                # Closing character matches the last opening character
                if open_chars:
                    open_chars.pop()
            else:
                if row_index not in corrupted_row_indexes:
                    syntax_error_score += syntax_error_points[char]
                    corrupted_row_indexes.append(row_index)

print(f'Corrupted Row Indexes:  {corrupted_row_indexes}')
print(f'Syntax Error Score:     {syntax_error_score}')


print("\n===================  PART 2  ======================\n")

char_completion_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# Discard corrupted rows
input_data = [row for row_index, row in enumerate(input_data) if row_index not in corrupted_row_indexes]

row_completion_scores = []
for row_index, row in enumerate(input_data):
    # Getting all opening chars
    open_chars = [ row[0] ]
    for index, char in enumerate(row[1:]):
        if char in chunk_pair.keys():
            open_chars.append(char)
        elif char in chunk_pair.values():
            if char == chunk_pair[open_chars[-1]]:
                if open_chars:
                    open_chars.pop()

    # Getting closing characters to all opened characters left
    close_chars = [ chunk_pair[open_char] for open_char in open_chars[::-1] ]

    # Finding completion score
    row_completion_score = 0
    for close_char in close_chars:
        row_completion_score = row_completion_score*5 + char_completion_scores[close_char]
    row_completion_scores.append(row_completion_score)

# Middle value of sorted scores
row_completion_scores.sort()
print(f'Completion scores middle value: {row_completion_scores[int(len(row_completion_scores) / 2)]}')
