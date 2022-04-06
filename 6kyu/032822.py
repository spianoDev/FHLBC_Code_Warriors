# https://www.codewars.com/kata/622de76d28bf330057cd6af8
# Level 6kyu

## Directions ##

# Every book has n pages with page numbers 1 to n.
# The summary is made by adding up the number of digits of all page numbers.
#
# Task: Given the summary, find the number of pages n the book has.
#
# Example
# If the input is summary=25, then the output must be n=17:
# The numbers 1 to 17 have 25 digits in total: 1234567891011121314151617.
#
# Be aware that you'll get enormous books having up to 100.000 pages.
#
# All inputs will be valid.

## Function ##

def amount_of_pages(summary):
    digits = ""
    i = 0
    while len(digits) <= summary:
        digits += str(i)
        i += 1
    return i-1

# ## Test Cases ##

amount_of_pages(5) # => 5
amount_of_pages(25) # => 17
amount_of_pages(1095) # => 401
amount_of_pages(185) # =>97
amount_of_pages(660) # => 256
