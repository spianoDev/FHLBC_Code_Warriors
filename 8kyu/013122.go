package main

import "fmt"

func main() {
	Well([]string{"good", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good"})
	Well([]string{"good", "bad", "bad", "bad", "bad"})
	Well([]string{"bad", "bad", "bad"})
}

func Well(x []string) string {
	goodCount := 0
	for _, status := range x {
		if status == "good" {
			goodCount += 1
		}
	}
	if goodCount == 0 {
		fmt.Println("Fail!")
		return "Fail!"
	} else if goodCount <= 2 {
		fmt.Println("Publish!")
		return "Publish!"
	} else {
		fmt.Println("I smell a series!")
		return "I smell a series!"
	}
}

// Test Cases

//package kata_test

import (
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
	//. "codewarrior/kata" (needed in website to run tests)
)
var _ = Describe("Test Example", func() {
	It("should test example values", func() {
		Expect(Well([]string{"bad", "bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"good", "bad", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"good", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good"})).To(Equal("I smell a series!"))
	})
})

//// Sample Test Cases
// package kata_test (needed in website to run sample tests but already imported above)
//
//import (
//	. "github.com/onsi/ginkgo"
//	. "github.com/onsi/gomega"
	//. "codewarrior/kata"
//)

var _ = Describe("Test Example", func() {
	It("should test example values", func() {
		Expect(Well([]string{"good", "bad", "good", "good", "bad", "good", "bad", "bad", "good", "bad", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "good", "good", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "good", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "bad", "good", "bad", "bad", "good", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "good", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "good", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"bad", "bad", "bad", "good", "bad", "good", "good", "bad", "bad", "bad", "bad", "good", "good"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "good", "bad", "bad", "bad", "bad", "good"})).To(Equal("Publish!"))
		Expect(Well([]string{"good", "bad", "bad", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "good", "bad", "good", "good", "good", "bad", "bad", "good"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "good", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "bad", "good", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"good", "bad", "bad", "bad", "bad", "good", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"good"})).To(Equal("Publish!"))
		Expect(Well([]string{"good", "good"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "bad", "good", "bad", "bad", "bad", "good", "bad", "bad", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"good", "bad", "good", "good", "bad", "bad", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "good", "bad", "bad", "bad", "good"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "good", "bad", "bad", "good", "bad", "good", "bad", "bad", "bad", "bad", "bad", "bad", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "good"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "good", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"good", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "good"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"bad", "bad", "good", "bad", "bad", "good", "bad", "bad", "bad", "bad", "bad", "good", "good", "bad", "good", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "bad", "bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "good", "bad", "bad", "bad"})).To(Equal("Publish!"))
		Expect(Well([]string{"bad", "bad", "good", "bad", "bad", "good", "bad", "good", "bad", "bad", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad"})).To(Equal("Fail!"))
		Expect(Well([]string{"good", "bad", "bad", "bad", "bad", "bad", "good", "good", "bad", "bad", "bad", "bad", "good", "bad", "bad"})).To(Equal("I smell a series!"))
		Expect(Well([]string{"bad", "bad", "bad", "bad", "bad", "good", "bad", "bad"})).To(Equal("Publish!"))
	})
})
