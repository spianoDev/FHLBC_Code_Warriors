package main

import (
	"fmt"
)

func main() {
	QuarterOf(11)
}

func QuarterOf(month int) int {
	quarter := month / 3
	// because the divisor rounds to the floor number, I need to calculate the remainder
	remainder := month % 3
	if remainder > 0 {
		quarter += 1
	}
	fmt.Println(quarter)
	return quarter
}

//QuarterOf(3) // => 1
//QuarterOf(8) // => 3
//QuarterOf(11) // => 4
