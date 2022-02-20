package main

import "fmt"

func main() {
	GooseFilter([]string{"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"})
	GooseFilter([]string{"Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"})
	GooseFilter([]string{"Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"})
}

func GooseFilter(birds []string) []string {
	//geese := []string{"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}
	noGeese := []string{}
	for _, bird := range birds {
		if bird != "African" && bird != "Roman Tufted" && bird != "Toulouse" && bird != "Pilgrim" && bird != "Steinbacher" {
			noGeese = append(noGeese, bird)
		}

	}
	fmt.Println(noGeese)
	return noGeese
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
		Expect(GooseFilter([]string{"African", "Roman Tufted", "Toulouse", "Pilgrim","Steinbacher"})).To(Equal([]string{}))
		Expect(GooseFilter([]string{"Mallard", "Barbary", "Hook Bill", "Blue Swedish","Crested"})).To(Equal([]string{"Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"}))
		Expect(GooseFilter([]string{"Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse","Blue Swedish"})).To(Equal([]string{"Mallard", "Hook Bill", "Crested", "Blue Swedish"}))
	})
//})

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
//	It("should test example values", func() {
//
//	})
//})
