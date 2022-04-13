# https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e
# Level 6kyu

## Directions ##

# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.
#
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately,
# starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC"
# (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII).
# The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
#
# Example:
#
# solution('XXI') # should return 21
# Help:
#
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

## Function ##

def solution(roman):
    total = 0
    nums = []
    fours = roman.replace('IV', '4')
    if 'IV' in roman:
        nums.append(4)
    nines = fours.replace('IX', '9')
    if 'IX' in fours:
        nums.append(9)
    forty = nines.replace('XL', '40')
    if 'XL' in nines:
        nums.append(40)
    ninety = forty.replace('XC', '90')
    if 'XC' in forty:
        nums.append(90)
    four_hundred = ninety.replace('CD', '400')
    if 'CD' in ninety:
        nums.append(400)
    nine_hundred = four_hundred.replace('CM', '900')
    if 'CM' in four_hundred:
        nums.append(900)

    for i, char in enumerate(nine_hundred):
        if char == 'I':
            total += 1
        elif char == 'V':
            total += 5
        elif char == 'X':
            total += 10
        elif char == 'L':
            total += 50
        elif char == 'C':
            total += 100
        elif char == 'D':
            total += 500
        elif char == 'M':
            total += 1000
    for num in nums:
        total += num
    print(total)
    return total
## Test Cases ##

solution('XXI') # => 21, 'XXI should == 21'
# solution('I') # => 1, 'I should == 1')
# solution('IV') # => 4, 'IV should == 4')
# solution('XL')
# solution('MCMXCIV')
# solution('MMVIII') # => 2008, 'MMVIII should == 2008')
# solution('MDCLXVI') # => 1666, 'MDCLXVI should == 1666')
