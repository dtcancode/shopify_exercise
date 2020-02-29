import itertools

# Given an input "bit pattern" which is a string containing only the characters '0', '1' and '?'
# output a list of all "bit strings" which match the pattern where '?' acts as a wild card.
# For example:
#  "" -> [""]
#  "1?" -> ["10", "11"]
#  "?01?" -> ["0010", "0011", "1010", "1011"]

# bit_pattern_input = "??"
# bit_pattern_input = "0?"
# bit_pattern_input = "?01?"
bit_pattern_input = "0?0?1?"
# print(bit_pattern_input)


def one_zero_permutations(repeat_amount):

    one_zero_list = [1, 0]

    one_zero_permutations_list_return = []
    for p in itertools.product(one_zero_list, repeat=repeat_amount):
        one_zero_permutations_list_return.append(p)

    return one_zero_permutations_list_return


def pattern_finder(pattern_finder_input):

    question_mark_amount = pattern_finder_input.count('?')

    one_zero_permutations_list = one_zero_permutations(question_mark_amount)

    pattern_finder_list_return = [""] * 2 ** question_mark_amount

    for index_perm, item_perm in enumerate(one_zero_permutations_list):
        # print(index_perm, item_perm)
        question_mark_count = 0
        for j, character in enumerate(pattern_finder_input):
            # print(j, character)
            if character == '?':
                # print(j, pattern_finder_input, question_mark_count)
                pattern_finder_list_return[index_perm] = (pattern_finder_list_return[index_perm] +
                                                         str(item_perm[question_mark_count]))
                question_mark_count += 1
            else:
                pattern_finder_list_return[index_perm] = pattern_finder_list_return[index_perm] + character

    return pattern_finder_list_return


print(pattern_finder(bit_pattern_input))

# print(list(enumerate(bit_pattern_to_find)))

'''
def pattern_finder(bit_pattern_input):
    question_mark_amount = bit_pattern_input.count('?')

    bit_string_list = [""] * question_mark_amount ** 2

    one_or_zero_amount = (question_mark_amount ** 2) / 2

    for j, character in enumerate(bit_pattern_input):
        if character == '?':
            for i, x in enumerate(bit_string_list):
                if j % 2 == 0:
                    bit_string_list[i] = bit_string_list[i] + str(0)
                else:
                    bit_string_list[i] = bit_string_list[i] + str(1)

            # then append 1 to some and 0 to other
        else:
            for i, x in enumerate(bit_string_list):
                bit_string_list[i] = bit_string_list[i] + character
            # append character to every item in list

    return bit_string_list
'''

'''
def pattern_finder(bit_pattern_input):
    question_mark_amount = bit_pattern_input.count('?')

    bit_string_list = [""] * 2 ** question_mark_amount

    # one_or_zero_amount = int((question_mark_amount ** 2) / 2)
    #
    # one_list = ['1'] * one_or_zero_amount
    #
    # zero_list = ['0'] * one_or_zero_amount
    #
    # one_and_zero_list = one_list + zero_list
    #
    # print(one_and_zero_list)

    for j, character in enumerate(bit_pattern_input):
        print(j)
        if character == '?':
            for i, x in enumerate(bit_string_list):
                if j % 2 == 0:
                    # print(j, i)
                    bit_string_list[i] = bit_string_list[i] + str(1)
                if j % 2 != 0:
                    # print(j, i)
                    bit_string_list[i] = bit_string_list[i] + str(0)
                # else:
                #     bit_string_list[i] = bit_string_list[i] + str(1)

            # then append 1 to some and 0 to other
        else:
            for i, x in enumerate(bit_string_list):
                bit_string_list[i] = bit_string_list[i] + character
            # append character to every item in list

    return bit_string_list
'''

# print(pattern_finder(bit_pattern_to_find))

# numbers = ['0', '1']
#
# patterns = ['a', 'b', 'c']
#
# permutations = [[numbers, patterns] for number in numbers for pattern in patterns]
# print(permutations)

