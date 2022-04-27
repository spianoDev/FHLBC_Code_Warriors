# https://www.codewars.com/kata/55c45be3b2079eccff00010f
# Level 6kyu

## Directions ##

# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
#
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

## Function ##
def num_in_word(text):
    for char in text:
        if char.isdigit():
            return int(char)
    return

def order(sentence):
    words = sentence.split(' ')
    answer = sorted(words, key=num_in_word)
    print(answer)
    return " ".join(answer)

## Test Cases ##

order("is2 Thi1s T4est 3a") # => "Thi1s is2 3a T4est"
# order("4of Fo1r pe6ople g3ood th5e the2") # => "Fo1r the2 g3ood 4of th5e pe6ople"
# order("") # => ""
