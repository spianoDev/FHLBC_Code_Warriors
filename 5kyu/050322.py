# https://www.codewars.com/kata/5902bc7aba39542b4a00003d
# Level 5kyu

## Directions ##

# Story
# A freak power outage at the zoo has caused all of the electric cage doors to malfunction and swing open...
#
# All the animals are out and some of them are eating each other!
#
# It's a Zoo Disaster!
# Here is a list of zoo animals, and what they can eat
#
# antelope eats grass
# big-fish eats little-fish
# bug eats leaves
# bear eats big-fish
# bear eats bug
# bear eats chicken
# bear eats cow
# bear eats leaves
# bear eats sheep
# chicken eats bug
# cow eats grass
# fox eats chicken
# fox eats sheep
# giraffe eats leaves
# lion eats antelope
# lion eats cow
# panda eats leaves
# sheep eats grass

# Kata Task
# INPUT
# A comma-separated string representing all the things at the zoo
#
# TASK
# Figure out who eats whom until no more eating is possible.
#
# OUTPUT
# A list of strings (refer to the example below) where:
#
# The first element is the initial zoo (same as INPUT)
# The last element is a comma-separated string of what the zoo looks like when all the eating has finished
# All other elements (2nd to last-1) are of the form X eats Y describing what happened
# Notes
# Animals can only eat things beside them
#
# Animals always eat to their LEFT before eating to their RIGHT
#
# Always the LEFTMOST animal capable of eating will eat before any others
#
# Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible
#
# Example
# Input
#
# "fox,bug,chicken,grass,sheep"
#
# Working
#
# 1	fox can't eat bug
# "fox,bug,chicken,grass,sheep"
# 2	bug can't eat anything
# "fox,bug,chicken,grass,sheep"
# 3	chicken eats bug
# "fox,chicken,grass,sheep"
# 4	fox eats chicken
# "fox,grass,sheep"
# 5	fox can't eat grass
# "fox,grass,sheep"
# 6	grass can't eat anything
# "fox,grass,sheep"
# 7	sheep eats grass
# "fox,sheep"
# 8	fox eats sheep
# "fox"
# Output
#
# ["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"]

## Function ##
import itertools

eat_tree = {
    'antelope':  ['grass'],
    'big-fish': ['little-fish'],
    'bug': ['leaves'],
    'bear': ['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],
    'chicken': ['bug'],
    'cow': ['grass'],
    'fox': ['chicken', 'sheep'],
    'giraffe': ['leaves'],
    'lion': ['antelope', 'cow'],
    'panda': ['leaves'],
    'sheep': ['grass'],
}

def who_eats_who(zoo):
    order = zoo.split(',')

    for i, thing in enumerate(order):
        # print(eat_tree.get(thing))
        if eat_tree.get(thing) is None:
            print('key does not exist')
            pass
        elif order[i] == eat_tree[thing][0]:
            print(f'{eat_tree[thing][0]} eats {order[i]}')
        elif order[i-1] == eat_tree[thing][0]:
            print(f'{order[i]} eats {order[i-1]}')

        # if eat_tree[animal] == animal_order[i+1]:
        #     print(f'{eat_tree[animal]} eats {animal_order[i+1]}')
        # else:
        #     pass
        # print(animal_order[i], animal_order[i+1])
# for index, this in enumerate(mylist):
#     for that in mylist[index+1:]:
#         compare(this, that)

    print(order)
    # Your code here
    return [zoo, zoo]

## Test Cases ##

input = "fox,bug,chicken,grass,sheep"
result = [
    "fox,bug,chicken,grass,sheep",
    "chicken eats bug",
    "fox eats chicken",
    "sheep eats grass",
    "fox eats sheep",
    "fox"
]
who_eats_who(input) # => result
