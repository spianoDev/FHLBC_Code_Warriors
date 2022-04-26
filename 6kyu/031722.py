# https://www.codewars.com/kata/554ca54ffa7d91b236000023
# Level 6kyu

## Directions ##

# Enough is enough!
# Alice and Bob were on a holiday.
# Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection.
# However, Charlie doesn't like these sessions, since the motive usually repeats.
# He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show
# the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number.
# Can you help them to remove numbers such that their list contains each number only up to N times, without changing the
# order?
#
# Task
# Given a list and a number, create a new list that contains each number of lst at most N times without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
# drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times,
# and then take 3, which leads to [1,2,3,1,2,3]. With list [20,37,20,21] and number 1, the result would be [20,37,21].

## Function ##

def delete_nth(order, max_e):
    new_lst = []
    for pic in order:
        if pic not in new_lst:
            new_lst.append(pic)
        elif order.count(pic) <= max_e:
            new_lst.append(pic)
        elif order.count(pic) > max_e:
            if new_lst.count(pic) < max_e:
                new_lst.append(pic)
            print(order.count(pic))

    print(new_lst)
    return new_lst


## Test Cases ##

# delete_nth([20,37,20,21], 1) # => [20,37,21]
# delete_nth([1,1,3,3,7,2,2,2,2], 3) # => [1, 1, 3, 3, 7, 2, 2, 2]
delete_nth([8, 50, 49, 26, 50, 40, 26, 25, 8, 10, 10, 50, 50, 26, 8, 40, 24, 40, 10, 10, 25, 50, 24, 26, 49, 40, 50,
            26, 40, 49, 40, 10, 40, 25, 50, 50, 26, 34, 25, 8, 40, 40, 8, 49, 10, 40, 10, 34, 40, 10, 24, 25, 25, 40, 34, 10, 25, 8, 8, 25, 8, 10],8)
# [8, 50, 49, 26, 50, 40, 26, 25, 8, 10, 10, 50, 50, 26, 8, 40, 24, 40, 10, 10, 25, 50, 24, 26, 49, 40, 50, 26, 40,
# 49, 40, 10, 40, 25, 50, 50, 26, 34, 25, 8, 40, 8, 49, 10, 10, 34, 10, 24, 25, 25, 34, 25, 8, 8, 25, 8]
