# https://www.codewars.com/kata/583952fbc23341c7180002fd
# Level 7kyu

## Directions ##

# You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return an object which includes the count of food options selected by the developers on the meetup sign-up form..
#
# For example, given the following input array:
#
# list1 = [
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
#     { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
# ]
# your function should return the following object (the order of properties does not matter):
#
# { 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
# Notes:
#
# The order of the meals count in the object does not matter.
# The count value should be a valid number.
# The input array will always be valid and formatted as in the example above.
# there are 5 possible meal options and the strings representing the selected meal option will always be formatted in the same way, as follows:
# 'standard', 'vegetarian', 'vegan', 'diabetic', 'gluten-intolerant'.

## Function ##

def order_food(lst):
    #dict of the orders
    food_order = {
        'vegetarian': 0,
        'standard': 0,
        'vegan': 0,
        'gluten-intolerant': 0,
        'diabetic': 0
    }
    for i in lst:
        if i['meal'] == 'vegetarian':
            food_order['vegetarian'] += 1
        elif i['meal'] == 'standard':
            food_order['standard'] += 1
        elif i['meal'] == 'vegan':
            food_order['vegan'] += 1
        elif i['meal'] == 'gluten-intolerant':
            food_order['gluten-intolerant'] += 1
        elif i['meal'] == 'diabetic':
            food_order['diabetic'] += 1
    # remove entries that have value of zero
    for key, order in dict(food_order).items():
        if order == 0:
            del food_order[key]
    return food_order
## Test Cases ##

list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]
# order_food(list1)

# => answer = { 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
list2 = [
    {'firstName': 'Mtutgc', 'lastName': 'Wf', 'country': 'Bxzhpheou', 'continent': 'Europe', 'age': 42, 'language': 'R', 'meal': 'standard'},
    {'firstName': 'Fuhipmsg', 'lastName': 'Outun', 'country': 'Paw', 'continent': 'Africa', 'age': 71, 'language': 'C', 'meal': 'gluten-intolerant'},
    {'firstName': 'Fhymegih', 'lastName': 'Vpgqxedf', 'country': 'Mfxztjdtpt', 'continent': 'Asia', 'age': 1, 'language': 'Java', 'meal': 'gluten-intolerant'},
    {'firstName': 'J', 'lastName': 'Cnwdw', 'country': 'Qi', 'continent': 'Oceania', 'age': 37, 'language': 'Java', 'meal': 'gluten-intolerant'},
    {'firstName': 'Xamrdh', 'lastName': 'Gqkaialroq', 'country': 'Avyfqy', 'continent': 'Asia', 'age': 63, 'language': 'R', 'meal': 'standard'},
    {'firstName': 'Uab', 'lastName': 'Oqhwveel', 'country': 'Ytedwj', 'continent': 'Oceania', 'age': 29, 'language': 'Ruby', 'meal': 'standard'},
    {'firstName': 'Vykfovw', 'lastName': 'Xivr', 'country': 'Hiirwqzs', 'continent': 'Oceania', 'age': 9, 'language': 'PHP', 'meal': 'vegetarian'},
    {'firstName': 'Gypod', 'lastName': 'Qoxztm', 'country': 'Imcmlybig', 'continent': 'Oceania', 'age': 32, 'language': 'Python', 'meal': 'gluten-intolerant'},
    {'firstName': 'Nc', 'lastName': 'Vhzr', 'country': 'Ofjid', 'continent': 'Africa', 'age': 93, 'language': 'Clojure', 'meal': 'vegan'},
    {'firstName': 'Hhbxclyzf', 'lastName': 'Nghzdhd', 'country': 'Lf', 'continent': 'Oceania', 'age': 50, 'language': 'Python', 'meal': 'vegetarian'},
    {'firstName': 'Cfgtkghks', 'lastName': 'Ysjlxzj', 'country': 'Appyy', 'continent': 'Europe', 'age': 83, 'language': 'Clojure', 'meal': 'diabetic'},
    {'firstName': 'Kkker', 'lastName': 'Eiltk', 'country': 'C', 'continent': 'Oceania', 'age': 78, 'language': 'Clojure', 'meal': 'standard'},
    {'firstName': 'Yynhokih', 'lastName': 'Pitkacjbeg', 'country': 'Njkhggkrs', 'continent': 'Europe', 'age': 46, 'language': 'R', 'meal': 'vegetarian'},
    {'firstName': 'Azr', 'lastName': 'Gm', 'country': 'Qx', 'continent': 'Oceania', 'age': 52, 'language': 'Ruby', 'meal': 'diabetic'},
    {'firstName': 'N', 'lastName': 'Qfi', 'country': 'Ojjwktki', 'continent': 'Asia', 'age': 52, 'language': 'Clojure', 'meal': 'diabetic'},
    {'firstName': 'Rrh', 'lastName': 'Bobpvse', 'country': 'Bbgrzwfdje', 'continent': 'Europe', 'age': 64, 'language': 'C', 'meal': 'vegan'},
    {'firstName': 'Tal', 'lastName': 'Ddufh', 'country': 'Sj', 'continent': 'Oceania', 'age': 84, 'language': 'Python', 'meal': 'vegetarian'},
    {'firstName': 'Ifuemkchfh', 'lastName': 'Milgop', 'country': 'M', 'continent': 'Americas', 'age': 44, 'language': 'R', 'meal': 'diabetic'},
    {'firstName': 'Xtdig', 'lastName': 'Owjmfajd', 'country': 'Aalg', 'continent': 'Oceania', 'age': 65, 'language': 'Javascript', 'meal': 'diabetic'},
    {'firstName': 'Vep', 'lastName': 'Rdysuec', 'country': 'Wyhrgd', 'continent': 'Asia', 'age': 10, 'language': 'Python', 'meal': 'vegetarian'},
    {'firstName': 'Yhssrx', 'lastName': 'Qlv', 'country': 'Fwdgdf', 'continent': 'Asia', 'age': 98, 'language': 'Python', 'meal': 'diabetic'},
    {'firstName': 'Otirt', 'lastName': 'Lbq', 'country': 'Gh', 'continent': 'Americas', 'age': 19, 'language': 'Javascript', 'meal': 'gluten-intolerant'},
    {'firstName': 'Lljbolbr', 'lastName': 'Glqqdz', 'country': 'Ngtl', 'continent': 'Americas', 'age': 71, 'language': 'R', 'meal': 'standard'},
    {'firstName': 'Zbkca', 'lastName': 'Tdqqecrjk', 'country': 'Dmrelxer', 'continent': 'Europe', 'age': 88, 'language': 'Javascript', 'meal': 'gluten-intolerant'},
    {'firstName': 'Rfgnbtpa', 'lastName': 'Lmzajutpgw', 'country': 'D', 'continent': 'Asia', 'age': 59, 'language': 'R', 'meal': 'gluten-intolerant'},
    {'firstName': 'Qjmgydiskd', 'lastName': 'Jdsrztbckg', 'country': 'Ibbz', 'continent': 'Oceania', 'age': 77, 'language': 'Javascript', 'meal': 'vegan'},
    {'firstName': 'Ysrvihlntc', 'lastName': 'Kzpq', 'country': 'Uzomjaeeei', 'continent': 'Oceania', 'age': 60, 'language': 'Clojure', 'meal': 'standard'},
    {'firstName': 'Pgtnjdcqe', 'lastName': 'Spxpbkqzx', 'country': 'Iqvg', 'continent': 'Oceania', 'age': 17, 'language': 'Clojure', 'meal': 'vegan'},
    {'firstName': 'Vgilraak', 'lastName': 'Esmnzpdc', 'country': 'Np', 'continent': 'Europe', 'age': 68, 'language': 'Clojure', 'meal': 'diabetic'},
    {'firstName': 'Xkasjdiuiy', 'lastName': 'Mntmdqxb', 'country': 'Sqpjbva', 'continent': 'Asia', 'age': 88, 'language': 'R', 'meal': 'standard'},
    {'firstName': 'Enqdqtg', 'lastName': 'Myhdmvdq', 'country': 'Ssjtjei', 'continent': 'Americas', 'age': 66, 'language': 'Python', 'meal': 'gluten-intolerant'},
    {'firstName': 'Guz', 'lastName': 'Hhgo', 'country': 'Jqswnlv', 'continent': 'Oceania', 'age': 44, 'language': 'Python', 'meal': 'vegetarian'},
    {'firstName': 'Yuqjyoh', 'lastName': 'Ckguenx', 'country': 'Pvzcwnsap', 'continent': 'Americas', 'age': 68, 'language': 'Python', 'meal': 'diabetic'},
    {'firstName': 'Laa', 'lastName': 'Wksdpoetfw', 'country': 'Sdamdgb', 'continent': 'Oceania', 'age': 88, 'language': 'PHP', 'meal': 'vegetarian'},
    {'firstName': 'Mnwhm', 'lastName': 'Ls', 'country': 'Meizwu', 'continent': 'Africa', 'age': 22, 'language': 'C', 'meal': 'diabetic'}
]
# order_food(list2)
# => answer = {'standard': 7, 'gluten-intolerant': 8, 'vegetarian': 7, 'vegan': 4, 'diabetic': 9}

list3 = [
    {'firstName': 'Xrjzs', 'lastName': 'W', 'country': 'N', 'continent': 'Asia', 'age': 33, 'language': 'R', 'meal': 'vegan'},
    {'firstName': 'Pmttrfds', 'lastName': 'Aw', 'country': 'Zoyij', 'continent': 'Africa', 'age': 92, 'language': 'C', 'meal': 'vegan'}
]

order_food(list3)
# => answer = {'vegan': 2}
