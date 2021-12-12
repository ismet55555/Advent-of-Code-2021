from pprint import pprint


print('\n-------------------------------------------\n')
print('                   DAY 8')
print('\n-------------------------------------------\n')

# Open and load data
with open('sample-1.txt', 'r') as open_file:
    rows = open_file.readlines()
input_data = [ (row.strip('\n')) for row in rows ]
pprint(input_data, width=120)

##############################################################################

print('\n===================  PART 1  ======================\n')

letters_per_digit = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}
unique_segments_digits = [1, 4, 7, 8]
unique_segments_values = [2, 4, 3, 7]

output_values =  [ row.split(' | ')[1] for row in input_data ]

total_unique_segments = 0
for output_value in output_values:
    for item in output_value.split(' '):
        if len(item) in unique_segments_values:
            total_unique_segments += 1

print(f'Output Values Unique Segments: {total_unique_segments}')


print('\n===================  PART 2  ======================\n')

# Map signal wires (a, b, etc) to digit segments (direction)
# Known digits:   1, 4, 7, 8
# Unknown digits: 0, 2, 3, 5, 6, 9

signal_patterns =  [ row.split(' | ')[0] for row in input_data ]
pprint(signal_patterns)

digits_pattern_known = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}
segment_num_to_letters = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g'
}
segment_letters_to_num = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7
}
segments_used_by_digits = {          # SEGMENT
    1: [0, 2, 3, 5, 6, 7, 8, 9],        # top
    2: [0, 4, 5, 6, 8, 9],              # top, left
    3: [0, 1, 2, 3, 4, 7, 8, 9],        # top, right
    4: [2, 3, 4, 5, 6, 8, 9],           # middle
    5: [0, 2, 6, 8],                    # bottom, left
    6: [0, 1, 3, 4, 5, 6, 7, 8, 9],     # bottom, right
    7: [0, 2, 3, 5, 6, 8, 9]            # bottom
}
digit_segments = {
    0: [1, 2, 3, 5, 6, 7],
    1: [3, 6],
    2: [1, 3, 4, 5, 7],
    3: [1, 3, 4, 6, 7],
    4: [2, 3, 4, 6],
    5: [1, 2, 4, 6, 7],
    6: [1, 2, 4, 5, 6, 7],
    7: [1, 3, 6],
    8: [1, 2, 3, 4, 5, 6, 7],
    9: [1, 2, 3, 4, 6, 7],
}



for signal_pattern in signal_patterns:
    print('===========================================')
    print(signal_pattern)

    current_segments = {
        1: [],  # top
        2: [],  # top, left
        3: [],  # top, right
        4: [],  # middle
        5: [],  # bottom, left
        6: [],  # bottom, right
        7: []   # bottom
    }

    # KNOWN ITEMS
    for pattern in signal_pattern.split(' '):
        print('')
        print(f'---------------  PATTERN: {pattern}  -------------------------')

        pattern_num = [ segment_letters_to_num[letter] for letter in pattern ]
        pattern_num.sort()

        # Check for unique digits
        if len(pattern) in unique_segments_values:
            digit_index = unique_segments_values.index(len(pattern))
            digit = unique_segments_digits[digit_index]

            digits_pattern_known[digit] = pattern_num
            digits_pattern_known[digit].sort()

            # Record this digit's segment 
            for segment, digits in segments_used_by_digits.items():
                if digit in digits:
                    print(f'Segment: {segment}')
                    current_segments[segment].append(digit)
                    current_segments[segment].sort()
        else:
            digit = 'UNKNOWN'

        print('The digits that have the segment:')
        pprint(current_segments)
        print(f'Pattern: {pattern:10} - {pattern_num} - Digit: {digit}')
        print('Digit with known patterns:')
        pprint(digits_pattern_known)

    # GETTING UNKONWS ?
    for pattern in signal_pattern.split(' '):
        pass


        # segment_numbers_for_pattern = []
        # for segment in pattern:
        #     segment_numbers_for_pattern.append(mapping[segment])
        # print(segment_numbers_for_pattern)









