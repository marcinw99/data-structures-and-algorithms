package main

import (
	"fmt"
	"strconv"
)

func fizzBuzz(n int) []string {
	output := make([]string, n)

	for i := 1; i <= n; i++ {
		var divisibleBy3 = i%3 == 0
		var divisibleBy5 = i%5 == 0

		currentString := ""

		if divisibleBy3 {
			currentString += "Fizz"
		}
		if divisibleBy5 {
			currentString += "Buzz"
		}

		if len(currentString) == 0 {
			currentString = strconv.Itoa(i)
		}

		output[i-1] = currentString
	}

	return output
}

func main() {
	fmt.Println(fizzBuzz(3))
	fmt.Println(fizzBuzz(15))
}

// time = O(n)
// space = O(1)
