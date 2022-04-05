# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
# Level 6kyu

## Directions ##

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the
# final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

## Function ##



# ## Test Cases ##

solution("asdfadsf") # => ['as', 'df', 'ad', 'sf']
solution("asdfads") # => ['as', 'df', 'ad', 's_']
solution("") # =>  []
solution("x") # => ["x_"]
