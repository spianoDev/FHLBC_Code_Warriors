# https://www.codewars.com/kata/52fb87703c1351ebd200081f
# Level 6kyu

## Directions ##

# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
#
# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"

## Function ##

def what_century(year):
    suffix = ['st', 'nd', 'rd', 'th']
    answer1 = 0
    answer2 = 0
    if year[2:] == '00':
        answer1 = int(year[0:2])
    else:
        answer2 = int(year[0:2]) + 1

    if year[1:2] == '0' and year[0:1] != '1':
        return str(answer1) + suffix[3] if answer1 else str(answer2) + suffix[0]
    elif year[1:2] == '1' and year[0:1] != '1':
        return str(answer1) + suffix[0] if answer1 else str(answer2) + suffix[1]
    elif year[1:2] == '2' and year[0:1] != '1':
        return str(answer1) + suffix[1] if answer1 else str(answer2) + suffix[2]
    elif year[1:2] == '3' and year[0:1] != '1':
        return str(answer1) + suffix[2] if answer1 else str(answer2) + suffix[3]
    else:
        return str(answer1) + suffix[3] if answer1 else str(answer2) + suffix[3]


## Test Cases ##

# print(what_century("2011")) # => "21st"
# print(what_century("2154")) # => "22nd"
# print(what_century("2259")) # => "23rd"
# print(what_century("1234")) # => "13th"
# print(what_century("1023")) # => "11th"

print(what_century("6985"))
