# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python
# Level 8kyu

## Directions ##

# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter;
# and month 11 (November), is part of the fourth quarter.

## Function ##

def quarter_of(month):
    return 1 if month <= 3 else 2 if month <= 6 else 3 if month <= 9 else 4

## Test Cases ##

# quarter_of(3) # => 1
# quarter_of(8) # => 3
quarter_of(11) # => 4

## GOLANG Solution ##

func QuarterOf(month int) int {
  quarter := month / 3
  # because the divisor rounds to the floor number, I need to calculate the remainder
  remainder := month % 3
  if remainder > 0 { quarter += 1 }
  return quarter
}


