# https://www.codewars.com/kata/5810ad962b321bac8f000178
# Level 6kyu

## Directions ##

# A normal deck of 52 playing cards contains suits 'H', 'C', 'D', 'S' - Hearts, Clubs, Diamonds, Spades respectively
# - and cards with values from Ace (1) to King (13): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
#
# Your Task
# Complete the function that returns a shuffled deck of 52 playing cards without repeats.
#
# Each card should have format "{suit} {value}", e.g. the Queen of Hearts is "H 12" and the Ace of Spades is "S 1".
# The order of the cards must be different each time the function is called.

# Cheated a bit on this one since there is a module with build in 'shuffle' program
# https://www.programiz.com/python-programming/examples/shuffle-card

## Function ##

# def shuffled_deck(cards):
#     new_deck = random.shuffle(cards)
#     # print(random.shuffle(cards))
#     for i in range(52):
#         print(new_deck[i][0], new_deck[i][1])
#     # return []
# Python program to shuffle a deck of card

# importing modules
import itertools
import random
def shuffled_deck():
    # make a deck of cards
    deck = list(itertools.product(range(1, 14), ['H', 'C', 'D', 'S']))

    # shuffle the cards
    random.shuffle(deck)

    shuffled = []
    for i in range(52):
        shuffled.append(deck[i][1] + ' ' + str(deck[i][0]))

    print(shuffled)
    return shuffled

## Test Cases ##

#
shuffled_deck()
