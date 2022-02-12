# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
# Level 8kyu

## Directions ##

# Write a function that checks if a given string (case insensitive) is a palindrome.

## Function ##

def is_palindrome(s):
    return True if s.lower() == s[::-1].lower() else False

## Test Cases ##

is_palindrome('a') # => True
is_palindrome('aba') # => True
is_palindrome('Abba') # => True
is_palindrome('malam') # => True
is_palindrome('walter') # => False
is_palindrome('kodok') # => True
is_palindrome('Kasue') # => False


