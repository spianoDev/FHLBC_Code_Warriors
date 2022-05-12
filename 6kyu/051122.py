# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
# Level 6kyu

## Directions ##

# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
#
# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

## Function ##
def is_valid_IP(s):
    ip_nums = s.split('.')
    print(ip_nums)
    if len(ip_nums) != 4:
        return False
    num_bits = []
    for bits in ip_nums:
        if not bits.isdigit():
            return False

        num_bit = int(bits)
        if num_bit > 255:
            return False
        elif str(num_bit) != bits:
            return False
        else:
            pass

    return True

## Test Cases ##

# is_valid_IP('12.255.56.1') # =>    True
# is_valid_IP('') # =>            False
# is_valid_IP('abc.def.ghi.jkl') # => False
# is_valid_IP('123.456.789.0') # =>  False
# is_valid_IP('12.34.56') # =>        False
# is_valid_IP('12.34.56 .1') # =>     False
# is_valid_IP('12.34.56.-1') # =>     False
# is_valid_IP('123.045.067.089') # => False
# is_valid_IP('127.1.1.0') # =>       True
# is_valid_IP('0.0.0.0') # =>          True
# is_valid_IP('0.34.82.53') # =>      True
is_valid_IP('192.168.1.300') # =>  False
