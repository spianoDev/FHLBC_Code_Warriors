# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3
# Level 7kyu

## Directions ##

# Your task is to remove all consecutive duplicate words from a string,
# leaving only first words entries. For example:
#
# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
#
# --> "alpha beta gamma delta alpha beta gamma delta"

## Function ##

def remove_consecutive_duplicates(s):
    no_dups = []
    word_list = s.split(" ")
    print(word_list)
    # edge case for word_list containing a single entry
    if len(word_list) <= 1:
        return s
    # compare each word with previous word
    for i in range(1, len(word_list)):
        if word_list[i-1] != word_list[i]:
            no_dups.append(word_list[i-1])
        else:
            pass
    # edge case for word_list containing only identical entries
    if len(no_dups) == 0 and word_list[-2] == word_list[-1]:
        no_dups.append(word_list[-1])
    # add the final word in the list if it doesn't match the penultimate word or doesn't exist in the no_dups list
    elif word_list[-2] != word_list[-1] or word_list[-1] != no_dups[-1]:
        no_dups.append(word_list[-1])

    print(" ".join(no_dups))
    return " ".join(no_dups)

## Test Cases ##

# remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')
# => 'alpha beta gamma delta alpha beta gamma delta'
remove_consecutive_duplicates('FcPqHG FcPqHG FcPqHG FcPqHG gJWpDc X X rBb DnSlVRF UzFptufuAmC UzFptufuAmC leIRBdRu Lt Lt Lt ZTXHmIAi ZTXHmIAi')
# => 'FcPqHG gJWpDc X rBb DnSlVRF UzFptufuAmC leIRBdRu Lt ZTXHmIAi'
remove_consecutive_duplicates('MAZUm MAZUm')
# => 'MAZUm'
remove_consecutive_duplicates('Zv Zv Zv')
# => 'Zv'


