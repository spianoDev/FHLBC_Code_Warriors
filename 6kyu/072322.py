# https://www.codewars.com/kata/58235a167a8cb37e1a0000db
# Level 6kyu

## Directions ##

# Winter is coming, you must prepare your ski holidays.
# The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves
# you have in your drawer.
#
# Given an array describing the color of each glove, return the number of pairs you can constitute,
# assuming that only gloves of the same color can form pairs.
#
# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)
#
# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

## Function ##
def number_of_pairs(gloves):
    glove_sort = {}
    for glove in gloves:
        if glove in glove_sort:
            glove_sort[glove] += 1
        else:
            glove_sort[glove] = 1
    count = 0
    for key, value in glove_sort.items():
        count += value//2
    return count
## Test Cases ##

# number_of_pairs(["red","red"]) # => 1
# number_of_pairs(["red","green","blue"]) # =>0
# number_of_pairs(["gray","black","purple","purple","gray","black"]) # => 3
# number_of_pairs([]) # => 0
number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]) # => 4
