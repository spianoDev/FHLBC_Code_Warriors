package main

import "fmt"

func main() {
	Greet("Ryan")
}

func Greet(name string) string {
	return fmt.Sprintf("Hello, %s how are you doing today?", name)
}
