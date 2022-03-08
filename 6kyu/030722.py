# https://www.codewars.com/kata/598106cb34e205e074000031
# Level 6kyu

## Directions ##

# The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
#
# But some of the rats are deaf and are going the wrong way!
#
# Kata Task
# How many deaf rats are there?
#
# Legend
# P = The Pied Piper
# O~ = Rat going left
# ~O = Rat going right
# Example
# ex1 ~O~O~O~O P has 0 deaf rats
#
# ex2 P O~ O~ ~O O~ has 1 deaf rat
#
# ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

## Function ##

def count_deaf_rats(town):
    # eliminate extra spaces
    town = town.replace(" ", "")
    # find the piper position
    piper = town.find("P")
    # split the string into two sections to count the deaf rats
    front_to_piper = town[:piper].split("~O")
    piper_to_back = [town[i:i+2] for i in range(piper+1, len(town), 2)]
    deaf_rats = 0
    for rat in front_to_piper:
        if rat != '':
            deaf_rats += 1
    for rat in piper_to_back:
        if rat == '~O':
            deaf_rats += 1
    return deaf_rats


## Test Cases ##

# count_deaf_rats("~O~O~O~O P") # => 0
# count_deaf_rats("P O~ O~ ~O O~") # => 1
# count_deaf_rats("~O~O~O~OP~O~OO~") # => 2
# count_deaf_rats("O~P~O") # => 2
count_deaf_rats("O~~O~OPO~~O")
count_deaf_rats("~O~O~O~O~O~O~OPO~O~~O~O~OO~O~") # => 3
