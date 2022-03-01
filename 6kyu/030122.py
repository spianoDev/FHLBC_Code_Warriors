# https://www.codewars.com/kata/582887f7d04efdaae3000090
# Level 6kyu

## Directions ##

# You will be given a sequence of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return a sequence which includes the developer who is the oldest.
# In case of a tie, include all same-age senior developers listed in the same order as they appeared in the original input array.
#
# For example, given the following input array:
#
# list1 = [
#   { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
#   { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
#   { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
#   { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
# ]
# your function should return the following array:
#
# [
#   { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
#   { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
# ]
# Notes:
#
# The input array will always be valid and formatted as in the example above and will never be empty.

## Function ##

def find_senior(lst):
    ages = []
    senior_devs = []
    # find all the ages of the devs
    for devs in lst:
        ages.append(devs['age'])
    # add only devs that match the highest age to the senior_devs list
    for devs in lst:
        if devs['age'] == max(ages):
            senior_devs.append(devs)
    return senior_devs




## Test Cases ##

list1 = [
    { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
    { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
    { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
    { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
# answer1 = [
#     { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
#     { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
# ]
find_senior(list1) # =>  answer1

list2 = [
    { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
    { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
    { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
]
# answer2 = [
#     { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
# ]
find_senior(list2) # => answer2

list3 = [
    { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
    { 'firstName': 'Fatima', 'lastName': 'K.', 'country': 'Saudi Arabia', 'continent': 'Asia', 'age': 21, 'language': 'Clojure' },
    { 'firstName': 'Mark', 'lastName': 'G.', 'country': 'Scotland', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
    { 'firstName': 'Nikola', 'lastName': 'H.', 'country': 'Serbia', 'continent': 'Europe', 'age': 29, 'language': 'Python' },
    { 'firstName': 'Jakub', 'lastName': 'I.', 'country': 'Slovakia', 'continent': 'Europe', 'age': 28, 'language': 'Java' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 89, 'language': 'JavaScript' },
    { 'firstName': 'Luka', 'lastName': 'J.', 'country': 'Slovenia', 'continent': 'Europe', 'age': 29, 'language': 'Clojure' },
    { 'firstName': 'Mariam', 'lastName': 'B.', 'country': 'Egypt', 'continent': 'Africa', 'age': 89, 'language': 'Python' },
]

answer3 = [
    { 'firstName': 'Alexander', 'lastName': 'F.', 'country': 'Russia', 'continent': 'Europe', 'age': 89, 'language': 'Java' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 89, 'language': 'JavaScript' },
    { 'firstName': 'Mariam', 'lastName': 'B.', 'country': 'Egypt', 'continent': 'Africa', 'age': 89, 'language': 'Python' },
]
find_senior(list3) # => answer3
