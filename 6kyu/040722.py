# https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e
# Level 6kyu

## Directions ##

# What date corresponds to the nth day of the year?
# The answer depends on whether the year is a leap year or not.
#
# Write a function that will help you determine the date if you know the number of the day in the year,
# as well as whether the year is a leap year or not.
# The function accepts the day number and a boolean value isLeap as arguments,
# and returns the corresponding date of the year as a string "Month, day".
# Only valid combinations of a day number and isLeap will be tested.
#
# Examples:
# * With input `41, false` => return "February, 10"
# * With input `60, false` => return "March, 1
# * With input `60, true` => return "February, 29"
# * With input `365, false` => return "December, 31"
# * With input `366, true` => return "December, 31"

## Function ##

import datetime
from datetime import date, timedelta

def get_day(day, is_leap):
    day_one = datetime.date(2021, 1, 1)
    day_one_leap = datetime.date(2020, 1, 1)
    if is_leap:
        month_day = day_one_leap + timedelta(days=day-1)
        return month_day.strftime('%B, %-d')
    else:
        month_day = day_one + timedelta(days=day-1)
        return month_day.strftime('%B, %-d')


## Test Cases ##

# get_day(15, False) # => "January, 15"
# get_day(41, False) # => "February, 10"
# get_day(59, False) # => "February, 28"
get_day(60, False) # => "March, 1"
# get_day(60, True) # => "February, 29"
# get_day(365, False) # => "December, 31"
get_day(366, True) # => "December, 31"
