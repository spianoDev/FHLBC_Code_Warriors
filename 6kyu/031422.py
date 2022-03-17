# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# Level 6kyu

## Directions ##

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative
# persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example (Input --> Output):
#
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

## Function ##

def multiply_digits(num, count):
    nums = [n for n in str(num)]
    new_num = 1

    for digit in nums:
        new_num *= int(digit)
    # count += 1
    if new_num < 10:
        print("this is the final count: ")
        print(count+1)
        return count+1
    else:
        print('this is the recursive count')
        print(count)
        multiply_digits(new_num, count+1)


# multiply_digits(39)

def persistence(n):
    if n > 9:
        multiply_digits(n, count=0)
    else:
        return 0




# ## Test Cases ##
#
# print(persistence(39)) # => 3
# persistence(4) # => 0
# print(persistence(25)) # => 2
print(persistence(999)) # => 4

