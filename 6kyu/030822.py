# https://www.codewars.com/kata/5ae840b8783bb4ef79000094
# Level 6kyu

## Directions ##

# Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.
#
# The keys in the given dictionaries can overlap. In that case you should combine all source values in an array.
# Duplicate values should be preserved.
#
# Here is an example:
#
# source1 = {"A": 1, "B": 2}
# source2 = {"A": 3}
#
# result = merge(source1, source2);
# // result should have this content: {"A": [1, 3]}, "B": [2]}

## Function ##

def merge(*dicts):
    combined_dict = {}
    for dict in dicts:
        for key, value in dict.items():
            if key in combined_dict:
                combined_dict[key].append(value)
            else:
                combined_dict.update(
                    {key: [value]}
                )
    print(dicts)
    print(combined_dict)
    return combined_dict


## Test Cases ##

# merge({},{},{}) # => {}
# merge({"A": 1, "B": 2, "C": 3}) # => {"A": [1], "B": [2], "C": [3]}
# merge({"A": 1}, {"B": 2}) # => {"A": [1], "B": [2]}
merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) # => {"A": [1, 4], "B": [2], "C": [3], "D": [5]}
