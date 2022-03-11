# https://www.codewars.com/kata/569d488d61b812a0f7000015
# Level 6kyu

## Directions ##

# A stream of data is received and needs to be reversed.
#
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
#
# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:
#
# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.
#
# The data is given in an array as such:
#
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

## Function ##

# for index, item in enumerate(items):
#     print(index, item)
#
# #if you want to start from 1 instead of 0
# for count, item in enumerate(items, start=1):
#     print(count, item)

def data_reverse(data):
    num_of_bytes = len(data)//8
    cycles = 1
    print(num_of_bytes)
    original_data = data
    reversed_data = []
    while cycles <= num_of_bytes:
        reversed_data.append(original_data[-8:])
        del original_data[-8:]
        print(original_data)
        cycles += 1
    print(sum(reversed_data, []))
    return sum(reversed_data, [])

## Test Cases ##

data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
data_reverse(data1) # => data2
#
# data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
# data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
# data_reverse(data3) # => data4
