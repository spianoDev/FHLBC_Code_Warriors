# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
# Level 6kyu

## Directions ##

# Write a function that takes a string of braces, and determines if the order of the braces is valid.
# It should return true if the string is valid, and false if it's invalid.
#
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
# Thanks to @arnedag for the idea!
#
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
#
# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.
#
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

## Function ##

def valid_braces(string):
    try:
        return eval(string)
    except TypeError:
        print('it is ok')
        return True
    except SyntaxError as err:
        print(str(err))
        # except ValueError as e:  # as e syntax added in ~python2.5
        if str(err) != "invalid syntax (<string>, line 1)":
            print('tr8e')
            return True
        else:
            print("caught!")
            return False
        # if err == 'invalid syntax (<string>, line1)':
        #     print('error found')
            # return False
    # else:
    #     print('true')
    #     return True



## Test Cases ##

# valid_braces( "()" ) # => True
# valid_braces( "(}" ) # => False
# valid_braces( "[]" ) # => True
# valid_braces("[(])") # => False
# valid_braces( "{}" ) # => True
# valid_braces( "{}()[]" ) # => True
# valid_braces( "([{}])" ) # => True
# valid_braces( "([}{])" ) # => False
# valid_braces( "{}({})[]" ) # => True
# valid_braces( "(({{[[]]}}))" ) # => True
valid_braces( "(((({{" ) # => False
# valid_braces( ")(}{][" ) # => False
# valid_braces( "())({}}{()][][" ) # => False
