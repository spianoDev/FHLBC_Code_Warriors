/* Golang Solution (created new for CodeWars!) */
package main

import (
	"fmt"
)

func main() {
	fmt.Println(SwitchItUp(22))
	SwitchItUp(22)
}

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

// Test Cases

//package kata_test
//
//import (
//	. "github.com/onsi/ginkgo"
//	. "github.com/onsi/gomega"
//	//. "codewarrior/kata" (needed in website to run tests)
//)
//var _ = Describe("Test Example", func() {
//	It("should test example values", func() {
//		Expect(SwitchItUp(3)).To(Equal("Three"))
//		Expect(SwitchItUp(8)).To(Equal("Eight"))
//		Expect(SwitchItUp(9)).To(Equal("Nine"))
//	})
//})
//
//// Sample Test Cases
//// package kata_test (needed in website to run sample tests but already imported above)
////
////import (
//	//. "github.com/onsi/ginkgo"
//	//. "github.com/onsi/gomega"
//	//. "codewarrior/kata"
////)
//
//var _ = Describe("Test Example", func() {
//	It("should test example values", func() {
//		Expect(SwitchItUp(3)).To(Equal("Three"))
//		Expect(SwitchItUp(0)).To(Equal("Zero"))
//		Expect(SwitchItUp(2)).To(Equal("Two"))
//		Expect(SwitchItUp(1)).To(Equal("One"))
//		Expect(SwitchItUp(8)).To(Equal("Eight"))
//		Expect(SwitchItUp(4)).To(Equal("Four"))
//		Expect(SwitchItUp(7)).To(Equal("Seven"))
//		Expect(SwitchItUp(9)).To(Equal("Nine"))
//		Expect(SwitchItUp(5)).To(Equal("Five"))
//		Expect(SwitchItUp(6)).To(Equal("Six"))
//		Expect(SwitchItUp(22)).To(Equal("Not valid. Enter a number between 0 and 9."))
//	})
//})
