# https://www.codewars.com/kata/57f222ce69e09c3630000212
# Level 8kyu

## Directions ##

# For every good kata idea there seem to be quite a few bad ones!
#
#    In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
#    If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'.
#    If there are no good ideas, as is often the case, return 'Fail!'.:

## Function ##

def well(x):
    count_good = 0
    # count the number of good responses in the list
    for idea in x:
        if idea == 'good':
            count_good += 1
        else:
            pass
    # return the appropriate response depending on the good/bad count
    # I use print statements to check my work ahead of putting the solution in CodeWars

    if count_good == 0 :
        print('Fail!')
        return 'Fail!'
    elif count_good <= 2 :
        print('Publish!')
        return 'Publish!'
    elif count_good > 2 :
        print('I smell a series!')
        return 'I smell a series!'

## Test Cases ##

# well(['bad', 'bad', 'bad']) # => 'Fail!'
# well(['good', 'bad', 'bad', 'bad', 'bad']) # => 'Publish!'
well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']) # => "I smell a series!"


