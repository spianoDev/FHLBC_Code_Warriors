# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python
# Level 8kyu

## Directions ##

# You'll be given a string, and have to return the sum of all characters as an int.
# The function should be able to handle all ASCII characters.
#
# uniTotal("a") == 97 uniTotal("aaa") == 291

## Function ##

def uni_total(s):
    total = 0
    for char in s:
        total += ord(char)
    return total

## Test Cases ##

# uni_total("") # => 0
# uni_total("abc") # => 294
# uni_total("Mary Had A Little Lamb") # => 1873
uni_total("Mary had a little lamb") # => 2001
uni_total("CodeWars rocks") # => 1370
uni_total("And so does Strive") # => 1661
