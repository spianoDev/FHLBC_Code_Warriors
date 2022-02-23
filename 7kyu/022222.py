# https://www.codewars.com/kata/56786a687e9a88d1cf00005d
# Level 7kyu

## Directions ##

# You are given a string of n lines, each substring being n characters long. For example:
#
# s = "abcd\nefgh\nijkl\nmnop"
#
# We will study the "horizontal" and the "vertical" scaling of this square of strings.
#
# A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').
#
# Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
# A v-vertical scaling of a string consists of replicating v times each part of the squared string.
#
# Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
# Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.
#
# Example: a = "abcd\nefgh\nijkl\nmnop"
# scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
# Printed:
#
# abcd   ----->   aabbccdd
# efgh            aabbccdd
# ijkl            aabbccdd
# mnop            eeffgghh
# eeffgghh
# eeffgghh
# iijjkkll
# iijjkkll
# iijjkkll
# mmnnoopp
# mmnnoopp
# mmnnoopp
# Task:
# Write function scale(str, k, v) k and v will be positive integers. If str == "" return "".

## Function ##

def scale(str, k, v):
    # edge case for empty string
    if str == "":
        return ""
    elements = str.split("\n")
    first_dimension = []
    first_dim_as_string = []
    second_dimension = []
    for element in elements:
        # multiply each char by k then add "\n"
        for i in range(len(elements)):
            first_dimension.append(element[i]*k)
        first_dimension.append("\n")
    # join the values
    first_dim_as_string.append("".join(first_dimension))
    # split the resulting string on the "\n" to add the second dimension removing the extra "\n"
    second_elements = first_dim_as_string[0].split("\n")[:-1]
    for element in second_elements:
        second_dimension.append((element + "\n")*v)
    # return the final value eliminating the extra "\n"
    return "".join(second_dimension)[:-1]

## Test Cases ##

a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
scale(a, 2, 3) # => r
# scale("", 5, 5) # => ""
# scale("Kj\nSH", 1, 2) # => "Kj\nKj\nSH\nSH"
