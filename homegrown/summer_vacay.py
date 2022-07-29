# TBD
# Level 6kyu (I think)

## Directions ##

# Summer Vacation!

# Directions
# You are planning a summer vacation with your family/friends.
# You have a list of locations and possible packing items (as string variables),
# but want to make sure you pack enough clothes and accessories for the trip.
# Write a function that takes in the number of people going on the vacation, the number of days for the trip,
# and the location.

# packing_list(num_people, num_days, location)

# The function should retrun a dictionary of the packing items and quantity of what to pack.

# Note:
# locations and packing_items are provided lists for this kata
# Some packing items like sunscreen can be shared but others like underwear require 1 item/day for each person traveling
# Some packing items like sneakers only require 1 item for each person
# Not all locations require the same accessories.
# For example:
# Camping does not require a bathing suit, but would require a travel hammock.
# Beach requires a towel, but not hiking shoes
# Assume each person will want fresh clothes (shirt, shorts, underwear, and socks) each day of vacation
# The order of the returned items does not matter

from math import ceil

locations = 'camping, beach, hiking, pool'
packing_items = 't-shirt, shorts, underwear, pajamas, socks, sneakers, sandals, hiking shoes, ' \
                'bathing suit, towel, travel hammock, sunscreen, 4 person tent, water bottle, ' \
                'toiletries, snacks, firewood, backpack, beach bag, big umbrella, travel chair, cooler, ' \
                'swim goggles, frisbee'

## Function ##

def packing_list(num_people, num_days, location):
    stuff_to_pack = packing_items.split(',')
    print(stuff_to_pack)
    # base dict of stuff all locations need
    base_stuff = {
        stuff_to_pack[0].lstrip(): 1 * num_days * num_people,
        stuff_to_pack[1].lstrip(): 1 * num_days * num_people,
        stuff_to_pack[2].lstrip(): 1 * num_days * num_people,
        stuff_to_pack[3].lstrip(): 1 * num_people,
        stuff_to_pack[11].lstrip(): 1,
        stuff_to_pack[13].lstrip(): 1 * num_people,
        stuff_to_pack[14].lstrip(): 1 * num_people,
        stuff_to_pack[15].lstrip(): 1 * num_days * num_people,
    }

    # create each location dicts
    camping_stuff = {
        stuff_to_pack[10].lstrip(): 1,
        stuff_to_pack[12].lstrip(): ceil(num_people / 4),
        stuff_to_pack[16].lstrip(): 1 * num_days,
    }
    beach_stuff = {}
    hiking_stuff = {}
    pool_stuff = {}

    for stuff in stuff_to_pack:
        if stuff.lstrip() == 'socks':
            camping_stuff[stuff.lstrip()] = 1 * num_days * num_people
            camping_stuff[stuff_to_pack[5].lstrip()] = 1 * num_people
            hiking_stuff[stuff.lstrip()] = 1 * num_days * num_people
            hiking_stuff[stuff_to_pack[7].lstrip()] = 1 * num_people
        elif stuff.lstrip() == 'sandals' or stuff.lstrip() == 'bathing suit' or stuff.lstrip() == 'towel':
            beach_stuff[stuff.lstrip()] = 1 * num_people
            pool_stuff[stuff.lstrip()] = 1 * num_people
        elif stuff.lstrip() == 'travel chair':
            beach_stuff[stuff.lstrip()] = 1 * num_people
            camping_stuff[stuff.lstrip()] = 1 * num_people
        elif stuff.lstrip() == 'swim goggles':
            pool_stuff[stuff.lstrip()] = 1 * num_people
    print(base_stuff)
    print(camping_stuff)
    print(hiking_stuff)
    print(beach_stuff)
    print(pool_stuff)
    if location == 'camping':
        return camping_stuff | base_stuff
    elif location == 'beach':
        return beach_stuff | base_stuff
    elif location == 'hiking':
        return hiking_stuff | base_stuff
    else:
        return pool_stuff | base_stuff

## Test Cases ##

packing_list(6, 3, 'beach')
