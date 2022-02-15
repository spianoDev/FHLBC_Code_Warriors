# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0
# Level 7kyu

## Directions ##

# Your job is to implement a function which returns the last D digits of an integer N as a list.
#
# Special cases:
# If D > (the number of digits of N), return all the digits.
# If D <= 0, return an empty list.
# Examples:
# N = 1
# D = 1
# result = [1]
#
# N = 1234
# D = 2
# result = [3, 4]
#
# N = 637547
# D = 6
# result = [6, 3, 7, 5, 4, 7]

## Function ##

def solution(n,d):
    new_list = []
    if d <= 0:
        return new_list
    # remove extra digits from n
    if len(str(n)) > d:
        n = str(n)[(-d)::]
    for digit in str(n):
        new_list.append(int(digit))
    return new_list

## Test Cases ##

# solution(1,1) # => [1]
solution(123767,4) # => [3,7,6,7]
# solution(0,1) # => [0]
solution(34625647867585,10) # => [5,6,4,7,8,6,7,5,8,5]
solution(1234,0) # => []
solution(24134,-4) # => []
# solution(1343,5) # => [1,3,4,3]


