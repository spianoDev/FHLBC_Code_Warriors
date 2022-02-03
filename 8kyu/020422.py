# https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7
# Level 8kyu

## Directions ##

# Write a function, goose_filter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
#
# The geese are any strings in the following array, which is pre-populated in your solution:
#
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:
#
# ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array:
#
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed.
# Note that all of the strings will be in the same case as those provided, and some elements may be repeated.

## Function ##
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    # create a new list
    no_geese = []
    # loop through the birds list
    for bird in birds:
        # conditional statement looking for the geese options and appending to new list if satisfied
        if bird != "African" and bird != "Roman Tufted" and bird != "Toulouse" and bird != "Pilgrim" and bird != "Steinbacher":
            no_geese.append(bird)
        else:
            pass
    return no_geese
## Test Cases ##

# goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])
# =>["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
# => ["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]
goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]) # =>[]

