# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# Level 6kyu

## Directions ##

# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

### NOTE: Looks like I solved this one in the past so this is a slightly more succinct solution ###
## Function ##

def find_outlier(integers):
    odds = []
    evens = []
    for num in integers:
        evens.append(num) if num % 2 == 0 else odds.append(num)
    return odds[0] if len(odds) == 1 else evens[0]



## Test Cases ##

find_outlier([2, 4, 6, 8, 10, 3]) # => 3
# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) # => 11
# find_outlier([160, 3, 1719, 19, 11, 13, -21]) # => 160
