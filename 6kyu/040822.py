# https://www.codewars.com/kata/59da47fa27ee00a8b90000b4
# Level 6kyu

## Directions ##

# Given a string of integers, return the number of odd-numbered substrings that can be formed.
#
# For example, in the case of "1341", they are 1, 1, 3, 13, 41, 341, 1341, a total of 7 numbers.
#
# solve("1341") = 7. See test cases for more examples.

## Function ##
# I got some major help with this one to understand how to gather all possible substrings
# https://stackoverflow.com/questions/22469997/how-to-get-all-the-contiguous-substrings-of-a-string-in-python

def solve(s):
    def get_all_substrings(input_string):
        length = len(input_string)
        return [input_string[i:j+1] for i in range(length) for j in range(i, length)]
    all_nums = get_all_substrings(s)
    count = 0
    for num in all_nums:
        if int(num) % 2 == 1:
            count += 1
    return count

## Test Cases ##

solve("1347") # => 7
# solve("1357") # => 10
# solve("13471") # => 12
# solve("134721") # => 13
# solve("1347231") # => 20
solve("13472315") # => 28
