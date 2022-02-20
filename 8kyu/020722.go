package main

import "fmt"

func main() {
	FindNeedle([]interface{}{"3", "123124234", nil, "needle", "world", "hay", 2, "3", true, false}, "needle")
	FindNeedle([]interface{}{"283497238987234", "a dog", "a cat", "some random junk", "a piece of hay", "needle", "something somebody lost a while ago"}, "needle")
	FindNeedle([]interface{}{1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3, 4, 2, 34, 234, 23, 4, 234, 324, 324, "needle", 1, 2, 3, 4, 5, 5, 6, 5, 4, 32, 3, 45, 54}, "needle")
}

func FindNeedle(haystack []interface{}, needle string) int {
	for i, v := range haystack {
		if v == needle {
			fmt.Println(i)
			return i
		}
	}
	return -1
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

//	})
//})
