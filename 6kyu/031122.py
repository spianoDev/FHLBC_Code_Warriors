# https://www.codewars.com/kata/559536379512a64472000053
# Level 6kyu

## Directions ##

# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they
# can be guessed due to common cultural references. You can get your passphrases stronger by different means.
# One is the following:
#
# choose a text in capital letters including or not digits and non alphabetic characters,
#
# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result.
# Example:
# your text: "BORN IN 2015!", shift 1
#
# 1 + 2 + 3 -> "CPSO JO 7984!"
#
# 4 "CpSo jO 7984!"
#
# 5 "!4897 Oj oSpC"

## Function ##

def play_pass(s, n):
    # function to find complement number
    def complement_num(num):
        return 9 - num
    transform = []
    # change the incoming 'n' to less than 26
    n = n % 26
    for char in s:
        if char.isalpha():
            new_char = ord(char.lower()) + n
            if new_char > 122:
                new_char = new_char - 26
            transform.append(chr(new_char))
        elif char.isdigit():
            transform.append(str(complement_num(int(char))))
        else:
            transform.append(char)
    final_transform = []
    for i, char in enumerate(transform):
        if char.isalpha():
            if i % 2 == 0:
                print(char)
                upper_char = char.replace(char, char.upper())
                final_transform.append(upper_char)
            else:
                final_transform.append(char)
        else:
            final_transform.append(char)

    print("". join(final_transform[::-1]) )
    return "". join(final_transform[::-1])





## Test Cases ##

# play_pass("I LOVE YOU!!!", 1) # => "!!!vPz fWpM J"
play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2)
# => "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"

