package main

import "fmt"

func main() {
	Well([]string{"good", "bad", "bad", "bad", "bad", "good", "bad", "bad", "good"})
}

func Well(x []string) string {
	for i, status := range x {
		fmt.Printf("Iteration %d: answer is %s \n", i, status)
	}
	return ""
}
