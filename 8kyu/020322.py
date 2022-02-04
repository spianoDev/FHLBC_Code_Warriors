# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031
# Level 8kyu

## Directions ##

# When provided with a number between 0-9, return it in words.
#   Input :: 1
#   Output :: "One".
#   If your language supports it, try using a switch statement.

## Function ##

# Python doesn't really support an easy way to use switch, but this would be the way to do it.
def switch_it_up(number):
    # make a dictionary of the possible answers
    case = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    print(case[number])
    return case[number]

## Test Cases ##

switch_it_up(0) # => "Zero"
switch_it_up(9) # => "Nine"

