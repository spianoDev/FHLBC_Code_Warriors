package main

import (
	"fmt"
	"strings"
)

func main() {
	IsPalindrome("a")
	IsPalindrome("aba")
	IsPalindrome("Abba")
	IsPalindrome("hello")
}

func IsPalindrome(str string) bool {
	reverse := ""
	for _, char := range str {
		reverse = string(char) + reverse
	}
	fmt.Println(reverse)
	return strings.ToLower(str) == strings.ToLower(reverse)
}
