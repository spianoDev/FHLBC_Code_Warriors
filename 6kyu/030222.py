# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
# Level 6kyu

## Directions ##

# Given an array of integers of any length, return an array that has 1 added to the value
# represented by the array.
#
# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.
#
# Examples
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
#
# [4, 3, 2, 5] would return [4, 3, 2, 6]

## Function ##

def up_array(arr):
    # handling for empty arr
    if len(arr) == 0:
        return None
    # handling for non int or negative numbers
    for num in arr:
        if not isinstance(num, int) or num < 0 or num >= 10:
            return None
    # join the array into a string number value
    number = ("".join(str(num) for num in arr))
    # increment this number
    new_num = int(number) + 1
    # create a new list of nums from the new_num string value
    return [int(num) for num in str(new_num)]



## Test Cases ##

up_array([2,3,9]) # => [2,4,0])
# up_array([4,3,2,5]), # => [4,3,2,6]
# up_array([1,-9]) # => None
# up_array(['hello']) # => None
up_array([]) # => None
