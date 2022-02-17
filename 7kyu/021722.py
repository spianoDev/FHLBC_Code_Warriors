# https://www.codewars.com/kata/59b11f57f322e5da45000254
# Level 7kyu

## Directions ##

# The Ones' Complement of a binary number is the number obtained by swapping all the 0s for 1s
# and all the 1s for 0s.
# For example:
# ones_complement(1001) = 0110
# ones_complement(1001) = 0110
# For any given binary number,formatted as a string, return the Ones' Complement of that number.

## Function ##

def ones_complement(binary_number):
    complement_binary = ""
    for num in binary_number:
        if num == "1":
            complement_binary += "0"
        else:
            complement_binary += "1"
    return complement_binary

## Test Cases ##

# ones_complement("0") # => "1"
# ones_complement("1") # => "0"
# ones_complement("01") # => "10"
ones_complement("10") # => "01"
ones_complement("1101") # => "0010"

