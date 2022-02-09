# https://www.codewars.com/kata/53dc23c68a0c93699800041d
# Level 8kyu

## Directions ##

# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
#
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

## Function ##

def smash(words):
    sentence = ""
    for word in words:
        sentence += word + " "
    return sentence[:-1]

## Test Cases ##

# smash(["hello", "world"]) # => "hello world"
smash(["hello", "amazing", "world"]) # => "hello amazing world"
smash(["this", "is", "a", "really", "long", "sentence"]) # => "this is a really long sentence"
