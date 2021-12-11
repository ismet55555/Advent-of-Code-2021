print("\n-------------------------------------------\n")
print("                   DAY 10")
print("\n-------------------------------------------\n")

from pprint import pprint

# Open and load data
with open("data.txt", "r") as open_file:
    rows = open_file.readlines()
data = [(row.strip("\n")) for row in rows]
pprint(data, width=50)

##############################################################################

'''
# SAMPLE OUTLINE:

INDEX   PATTERN                     STATUS      ERROR                             SCORE
0       [({(<(())[]>[[{[]{<()<>>    incomplete
1       [(()[<>])]({[<{<<[]>>(      incomplete
2       {([(<{}[<>[]}>{[]{[(<()>    corrupted - Expected ], but found } instead - 1197
3       (((({<>}<{<{<>}{[]{[]{}     incomplete
4       [[<[([]))<([[{}[[()]]]      corrupted - Expected ], but found ) instead - 3
5       [{[{({}]{}}([{[{{{}}([]     corrupted - Expected ), but found ] instead - 57
6       {<[[]]>}<{[{[{[]{()[[[]     incomplete
7       [<(<(<(<{}))><([]([]()      corrupted - Expected >, but found ) instead - 3
8       <{([([[(<>()){}]>(<<{{      corrupted - Expected ], but found > instead - 25137
9       <{([{{}}[<[[[<>{}]]]>[]]    incomplete

TOTAL: 3 + 3 + 57 + 1197 + 25137 = 26397
'''

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

sample_answers = {
    0: 'incomplete',
    1: 'incomplete',
    2: 'corrupted - Expected ], but found } instead',
    3: 'incomplete',
    4: 'corrupted - Expected ], but found ) instead',
    5: 'corrupted - Expected ), but found ] instead',
    6: 'incomplete',
    7: 'corrupted - Expected >, but found ) instead',
    8: 'corrupted - Expected ], but found > instead',
    9: 'incomplete',
}

#                |
# [{}[()[[]]]()][}
#                   |
# <{([([ [(<>()){}] >(<<{{


syntax_error_score = 0

for row_index, row in enumerate(data):
    print(f'\n\n=========== {row_index} ==============')
    print(row)
    # print(sample_answers[row_index])

    opens = [ row[0] ]
    corrupt_syntax = False

    # Finding incomplete chunk opening chars
    for index, char in enumerate(row[1:]):
        print(f'\n---- {char} -----')
        print(f'    Last open: {opens[-1] if opens else "NONE"}')

        if char in chunk_pair.keys():
            # Opening Chunk
            print(f'OPEN: {char}')
            opens.append(char)
        elif char in chunk_pair.values():
            # Closing Chunk
            print(f'CLOSE: {char}')
            if char == chunk_pair[opens[-1]]:
                print('MATCH CLOSE')
                if opens:
                    opens.pop()
            else:
                print('CORRUPT !!!! AAAAHHH')
                if not corrupt_syntax:
                    corrupt_syntax = True
                    syntax_error_score += syntax_error_points[char]
    if opens:
        print('Syntax Incomplete:   True')
    if corrupt_syntax:
        print('Syntax Corrupt:      True')

print(f'Syntax Error Score: {syntax_error_score}')



print("\n===================  PART 2  ======================\n")


