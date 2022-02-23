# https://www.codewars.com/kata/56786a687e9a88d1cf00005d
# Level 7kyu

## Directions ##

# You are going to be given a word.
# Your job will be to make sure that each character in that word has the exact same number of occurrences.
# You will return true if it is valid, or false if it is not.
#
# For this kata, capitals are considered the same as lowercase letters.
# Therefore: "A" == "a"
#
# The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols.
# The length will be 0 < length < 100.
#
# Examples
# "abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
# "abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!
# "123abc!" is a valid word because all of the characters only appear once in the word.

## Function ##

def validate_word(word):
    char_counter = {}
    # create a character counter
    for char in word:
        if char.lower() in char_counter:
            char_counter[char.lower()] += 1
        else:
            char_counter[char.lower()] = 1
    # return true if the first value is the same as all values in char_counter
    first_char_value = list(char_counter.values())[0]
    return all(count==first_char_value for count in char_counter.values())


## Test Cases ##

# validate_word("abcabc") # => True
# validate_word("Abcabc") # => True
validate_word("AbcabcC") # => False
# validate_word("AbcCBa") # => True
# validate_word("pippi") # => False
# validate_word("?!?!?!") # => True
# validate_word("abc123") # => True
# validate_word("abcabcd") # => False
# validate_word("abc!abc!") # => True
# validate_word("abc:abc") # => False



