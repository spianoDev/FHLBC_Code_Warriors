package main

func main() {
	BooleanToString(true)
	BooleanToString(false)
}

func BooleanToString(b bool) string {
	if b == true {
		//fmt.Println("True")
		return "True"
	} else {
		//fmt.Println("False")
		return "False"
	}
}

// Test Cases

package kata_test

import (
. "github.com/onsi/ginkgo"
. "github.com/onsi/gomega"
//. "codewarrior/kata" (needed in website to run tests)
)
var _ = Describe("Test Example", func() {
	It("should test example values", func() {
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
	})
})

//
////// Sample Test Cases
//// package kata_test (needed in website to run sample tests but already imported above)
////
////import (
////	. "github.com/onsi/ginkgo"
////	. "github.com/onsi/gomega"
////. "codewarrior/kata"
////)
//
//var _ = Describe("Test Example", func() {
	It("should test example values", func() {
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(false)).To(Equal("False"))
		Expect(BooleanToString(true)).To(Equal("True"))
		Expect(BooleanToString(false)).To(Equal("False"))
	})
//})
