# https://www.codewars.com/kata/56747fd5cb988479af000028
# Level 7kyu

## Directions ##

# You are going to be given a word. Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.
#
# #Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"
# #Input
#
# A word (string) of length 0 < str < 1000
# This is only here to tell you that you do not need to worry about your solution timing out.
#
# #Output
#
# The middle character(s) of the word represented as a string.

## Function ##

def get_middle(s):
    midpoint = len(s)//2
    remainder = len(s)%2
    if midpoint == 0 and remainder == 1:
        return s[midpoint]
    elif midpoint == 1 and remainder == 0:
        return s[midpoint-1] + s[midpoint]
    elif midpoint > 1 and remainder == 0:
        return s[midpoint-1] + s[midpoint]
    else:
        return s[midpoint]

## Test Cases ##

get_middle("test") # => "es"
get_middle("testing") # => "t"
get_middle("middle") # => "dd"
get_middle("A") # => "A"
get_middle("of") # => "of"


