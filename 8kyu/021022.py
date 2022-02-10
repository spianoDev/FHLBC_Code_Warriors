# https://www.codewars.com/kata/55a70521798b14d4750000a4
# Level 8kyu

## Directions ##

# Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".
#
# [Make sure you type the exact thing I wrote or the program may not execute properly]

## Function ##

def greet(name):
    return "Hello, %s how are you doing today?" % name

## Test Cases ##

greet('Ryan') # => "Hello, Ryan how are you doing today?"
greet('Shingles') # => "Hello, Shingles how are you doing today?"
