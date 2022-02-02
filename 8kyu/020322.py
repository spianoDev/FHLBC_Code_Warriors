# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031
# Level 8kyu

## Directions ##

# When provided with a number between 0-9, return it in words.
#   Input :: 1
#   Output :: "One".
#   If your language supports it, try using a switch statement.

## Function ##

# Python doesn't really support an easy way to use switch, but this would be the way to do it.
def switch_it_up(number):
    # make a dictionary of the possible answers
    case = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    print(case[number])
    return case[number]

## Test Cases ##

switch_it_up(0) # => "Zero"
switch_it_up(9) # => "Nine"

## Golang Solution (created new for CodeWars!) ##

package kata

func SwitchItUp(number int) string {
  strNums := []string{"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
  switch number {
    case 0:
        return strNums[0]
    case 1:
        return strNums[1]
    case 2:
        return strNums[2]
    case 3:
        return strNums[3]
    case 4:
        return strNums[4]
    case 5:
        return strNums[5]
    case 6:
        return strNums[6]
    case 7:
        return strNums[7]
    case 8:
        return strNums[8]
    case 9:
        return strNums[9]
       }
    return "Not valid. Enter a number between 0 and 9."
    }
}

## Test Cases ##
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Test Example", func() {
  It("should test example values", func() {
    Expect(SwitchItUp(3)).To(Equal("Three"))
    Expect(SwitchItUp(8)).To(Equal("Eight"))
    Expect(SwitchItUp(9)).To(Equal("Nine"))
  })
})

## Sample Test Cases ##
package kata_test
import (
  . "github.com/onsi/ginkgo"
  . "github.com/onsi/gomega"
  . "codewarrior/kata"
)
var _ = Describe("Test Example", func() {
  It("should test example values", func() {
    Expect(SwitchItUp(3)).To(Equal("Three"))
    Expect(SwitchItUp(0)).To(Equal("Zero"))
    Expect(SwitchItUp(2)).To(Equal("Two"))
    Expect(SwitchItUp(1)).To(Equal("One"))
    Expect(SwitchItUp(8)).To(Equal("Eight"))
    Expect(SwitchItUp(4)).To(Equal("Four"))
    Expect(SwitchItUp(7)).To(Equal("Seven"))
    Expect(SwitchItUp(9)).To(Equal("Nine"))
    Expect(SwitchItUp(5)).To(Equal("Five"))
    Expect(SwitchItUp(6)).To(Equal("Six"))
    Expect(SwitchItUp(22)).To(Equal("Not valid. Enter a number between 0 and 9."))
  })
})
