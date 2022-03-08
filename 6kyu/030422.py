# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
# Level 6kyu

## Directions ##

# Write a function that takes a str of braces, and determines if the order of the braces is valid.
# It should return true if the str is valid, and false if it's invalid.
#
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}.
# Thanks to @arnedag for the idea!
#
# All input strs will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
#
# What is considered Valid?
# A str of braces is considered valid if all braces are matched with the correct brace.
#
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

## Function ##

# def valid_braces(str):
#     try:
#         return eval(str)
#     except TypeError:
#         print('it is ok')
#         return True
#     except SyntaxError as err:
#         print(str(err))
#         # except ValueError as e:  # as e syntax added in ~python2.5
#         if str(err) != "invalid syntax (<str>, line 1)":
#             print('tr8e')
#             return True
#         else:
#             print("caught!")
#             return False
#         # if err == 'invalid syntax (<str>, line1)':
#         #     print('error found')
#             # return False
#     # else:
#     #     print('true')
#     #     return True

def valid_braces(str):
    brace_options = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    while len(str) > 1:
        if len(str) > str.find("{") >= 0:
            if str.find("}") != -1 and str.find("}") > str.find("{"):
                str = str[:str.find("{")] + str[str.find("}")+1:]
            else:
                return False
        elif len(str) > str.find("[") >= 0:
            if str.find("]") != -1 and str.find("]") > str.find("["):
                str = str[:str.find("[")] + str[str.find("]")+1:]
            else:
                return False
        elif len(str) > str.find("(") >= 0:
            if str.find(")") != -1 and str.rfind(")") > str.find("("):
                str = str[:str.find("(")] + str[str.rfind(")")+1:]
            else:
                return False
    return len(str) == 0



## Test Cases ##

# valid_braces( "()" ) # => True
# valid_braces( "(}" ) # => False
# valid_braces( "[]" ) # => True
# valid_braces("[(])") # => False
# valid_braces( "{}" ) # => True
# valid_braces( "{}()[]" ) # => True
# valid_braces( "([{}])" ) # => True
valid_braces( "([}{])" ) # => False
# valid_braces( "{}({})[]" ) # => True
# valid_braces( "(({{[[]]}}))" ) # => True
# valid_braces( "(((({{" ) # => False
# valid_braces( ")(}{][" ) # => False
# valid_braces( "())({}}{()][][" ) # => False
