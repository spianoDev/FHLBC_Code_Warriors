package main

import "fmt"

func main() {
	GooseFilter([]string{"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"})
	GooseFilter([]string{"Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"})
	GooseFilter([]string{"Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"})
}

func GooseFilter(birds []string) []string {
	geese := []string{"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}
	noGeese := []string{}
	for _, bird := range birds {
		if bird != geese[0] && bird != geese[1] && bird != geese[2] && bird != geese[3] && bird != geese[4] {
			noGeese = append(noGeese, bird)
		}
	}
	fmt.Println(noGeese)
	return noGeese
}

// Test Cases
//
//package kata_test
//
//import (
//. "github.com/onsi/ginkgo"
//. "github.com/onsi/gomega"
////. "codewarrior/kata" (needed in website to run tests)
//)
//var _ = Describe("Test Example", func() {
	It("should test example values", func() {
		Expect(GooseFilter([]string{"African", "Roman Tufted", "Toulouse", "Pilgrim","Steinbacher"})).To(Equal([]string{}))
		Expect(GooseFilter([]string{"Mallard", "Barbary", "Hook Bill", "Blue Swedish","Crested"})).To(Equal([]string{"Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"}))
		Expect(GooseFilter([]string{"Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse","Blue Swedish"})).To(Equal([]string{"Mallard", "Hook Bill", "Crested", "Blue Swedish"}))
	})
//})

// Sample Test Cases
// package kata_test (needed in website to run sample tests but already imported above)
//
//import (
//	. "github.com/onsi/ginkgo"
//	. "github.com/onsi/gomega"
//. "codewarrior/kata"
//)
//
var _ = Describe("Test Example", func() {
	It("should test example values", func() {
		Expect(GooseFilter([]string{"Hawkgirl", "Pippi", "African", "Harpy", "Tiamat", "Protoss Carrier"})).To(Equal([]string{"Hawkgirl", "Pippi", "Harpy", "Tiamat", "Protoss Carrier"}))
		Expect(GooseFilter([]string{"Roman Tufted", "Crested", "Infernal Hawk", "African", "Hook Bill", "Kinto-kun", "Hawkgirl", "Protoss Carrier", "Pippi", "Roc", "Pilgrim", "Toulouse", "Tiamat", "Steinbacher", "Red Dragon", "Harpy", "Zerg Leviathan", "Blue Swedish"})).To(Equal([]string{"Crested", "Infernal Hawk", "Hook Bill", "Kinto-kun", "Hawkgirl", "Protoss Carrier", "Pippi", "Roc", "Tiamat", "Red Dragon", "Harpy", "Zerg Leviathan", "Blue Swedish"}))
		Expect(GooseFilter([]string{"Toulouse", "Phoenix", "Roc", "Red Dragon", "African", "Zerg Leviathan", "Tiamat", "Blue Swedish", "Celestial Eagle", "Pilgrim", "Mallard", "Manbat", "Protoss Carrier", "Pippi", "Steinbacher", "Hook Bill", "Infernal Hawk", "Hawkgirl", "Kinto-kun", "Crested"})).To(Equal([]string{"Phoenix", "Roc", "Red Dragon", "Zerg Leviathan", "Tiamat", "Blue Swedish", "Celestial Eagle", "Mallard", "Manbat", "Protoss Carrier", "Pippi", "Hook Bill", "Infernal Hawk", "Hawkgirl", "Kinto-kun", "Crested"}))
		Expect(GooseFilter([]string{"Zerg Leviathan", "Manbat", "Hawkgirl", "Roman Tufted", "Crested", "Toulouse", "Terran Battlecruiser", "Kinto-kun", "Steinbacher", "Red Dragon", "Celestial Eagle", "Pippi"})).To(Equal([]string{"Zerg Leviathan", "Manbat", "Hawkgirl", "Crested", "Terran Battlecruiser", "Kinto-kun", "Red Dragon", "Celestial Eagle", "Pippi"}))
		Expect(GooseFilter([]string{"Celestial Eagle", "Pilgrim", "Blue Swedish", "Phoenix", "Roman Tufted", "African", "Steinbacher", "Tiamat", "Protoss Carrier", "Manbat", "Harpy", "Pippi", "Red Dragon", "Roc", "Crested", "Wyvern", "Infernal Hawk", "Toulouse", "Kinto-kun", "Hook Bill"})).To(Equal([]string{"Celestial Eagle", "Blue Swedish", "Phoenix", "Tiamat", "Protoss Carrier", "Manbat", "Harpy", "Pippi", "Red Dragon", "Roc", "Crested", "Wyvern", "Infernal Hawk", "Kinto-kun", "Hook Bill"}))
		Expect(GooseFilter([]string{"Celestial Eagle"})).To(Equal([]string{"Celestial Eagle"}))
		Expect(GooseFilter([]string{"Roman Tufted", "Crested", "Hook Bill", "Red Dragon", "Kinto-kun", "Infernal Hawk", "Steinbacher", "Manbat", "Mallard", "Pippi"})).To(Equal([]string{"Crested", "Hook Bill", "Red Dragon", "Kinto-kun", "Infernal Hawk", "Manbat", "Mallard", "Pippi"}))
		Expect(GooseFilter([]string{"Blue Swedish", "Harpy", "Roc", "Roman Tufted", "Hawkgirl", "Tiamat", "Red Dragon"})).To(Equal([]string{"Blue Swedish", "Harpy", "Roc", "Hawkgirl", "Tiamat", "Red Dragon"}))
		Expect(GooseFilter([]string{"Kinto-kun", "African", "Harpy", "Pilgrim", "Terran Battlecruiser", "Crested", "Manbat", "Tiamat", "Hawkgirl", "Celestial Eagle", "Mallard"})).To(Equal([]string{"Kinto-kun", "Harpy", "Terran Battlecruiser", "Crested", "Manbat", "Tiamat", "Hawkgirl", "Celestial Eagle", "Mallard"}))
		Expect(GooseFilter([]string{"Kinto-kun", "Manbat", "Pilgrim","Steinbacher"})).To(Equal([]string{"Kinto-kun", "Manbat"}))
		Expect(GooseFilter([]string{"Toulouse", "Zerg Leviathan", "Red Dragon", "Pilgrim", "Infernal Hawk", "Tiamat", "Hook Bill", "Terran Battlecruiser", "Mallard", "Protoss Carrier", "Harpy", "Blue Swedish", "Wyvern", "Crested", "African", "Steinbacher", "Phoenix", "Pippi", "Manbat", "Hawkgirl"})).To(Equal([]string{"Zerg Leviathan", "Red Dragon", "Infernal Hawk", "Tiamat", "Hook Bill", "Terran Battlecruiser", "Mallard", "Protoss Carrier", "Harpy", "Blue Swedish", "Wyvern", "Crested", "Phoenix", "Pippi", "Manbat", "Hawkgirl"}))
		Expect(GooseFilter([]string{"Wyvern", "African", "Steinbacher", "Roman Tufted", "Pippi", "Roc", "Harpy", "Kinto-kun", "Mallard", "Tiamat"})).To(Equal([]string{"Wyvern", "Pippi", "Roc", "Harpy", "Kinto-kun", "Mallard", "Tiamat"}))
		Expect(GooseFilter([]string{"Mallard"})).To(Equal([]string{"Mallard"}))
		Expect(GooseFilter([]string{"Terran Battlecruiser", "Roman Tufted", "Mallard", "Celestial Eagle", "Pippi", "Manbat", "Wyvern", "Pilgrim", "Hawkgirl", "Hook Bill", "Toulouse", "Red Dragon", "Protoss Carrier"})).To(Equal([]string{"Terran Battlecruiser", "Mallard", "Celestial Eagle", "Pippi", "Manbat", "Wyvern", "Hawkgirl", "Hook Bill", "Red Dragon", "Protoss Carrier"}))
		Expect(GooseFilter([]string{"Pilgrim", "Steinbacher", "Terran Battlecruiser", "Wyvern", "Infernal Hawk"})).To(Equal([]string{"Terran Battlecruiser", "Wyvern", "Infernal Hawk"}))
		Expect(GooseFilter([]string{"Tiamat", "Red Dragon", "Zerg Leviathan", "Hook Bill", "African", "Infernal Hawk", "Hawkgirl", "Toulouse", "Protoss Carrier", "Phoenix", "Blue Swedish", "Roman Tufted", "Kinto-kun", "Mallard", "Wyvern", "Crested", "Harpy", "Celestial Eagle", "Steinbacher"})).To(Equal([]string{"Tiamat", "Red Dragon", "Zerg Leviathan", "Hook Bill", "Infernal Hawk", "Hawkgirl", "Protoss Carrier", "Phoenix", "Blue Swedish", "Kinto-kun", "Mallard", "Wyvern", "Crested", "Harpy", "Celestial Eagle"}))
		Expect(GooseFilter([]string{"Toulouse", "Crested", "Phoenix", "Zerg Leviathan", "Terran Battlecruiser", "African"})).To(Equal([]string{"Crested", "Phoenix", "Zerg Leviathan", "Terran Battlecruiser"}))
		Expect(GooseFilter([]string{"Steinbacher", "Manbat", "Pilgrim", "Hook Bill", "Roc", "Protoss Carrier", "Blue Swedish", "Hawkgirl", "Roman Tufted", "Pippi", "Phoenix", "Infernal Hawk", "Toulouse"})).To(Equal([]string{"Manbat", "Hook Bill", "Roc", "Protoss Carrier", "Blue Swedish", "Hawkgirl", "Pippi", "Phoenix", "Infernal Hawk"}))
		Expect(GooseFilter([]string{"Phoenix", "Roc", "Roman Tufted"})).To(Equal([]string{"Phoenix", "Roc"}))
		Expect(GooseFilter([]string{"Protoss Carrier", "Mallard", "Pippi", "Terran Battlecruiser", "Celestial Eagle", "Zerg Leviathan"})).To(Equal([]string{"Protoss Carrier", "Mallard", "Pippi", "Terran Battlecruiser", "Celestial Eagle", "Zerg Leviathan"}))
		Expect(GooseFilter([]string{"Roman Tufted", "Crested", "Manbat"})).To(Equal([]string{"Crested", "Manbat"}))
	})
})
