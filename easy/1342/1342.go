package main

import "fmt"

func numberOfSteps(num int) int {
	remainingNumber := num
	amountOfStepsTaken := 0

	// bitwise approach
	for remainingNumber > 0 {
		if remainingNumber&1 == 0 {
			remainingNumber >>= 1
		} else {
			remainingNumber--
		}
		amountOfStepsTaken++
	}

	/*
		for remainingNumber > 0 {
			if remainingNumber%2 == 0 {
				remainingNumber /= 2
			} else {
				remainingNumber--
			}
			amountOfStepsTaken++
		}
	*/

	return amountOfStepsTaken
}

func main() {
	fmt.Println(numberOfSteps(14))
}

// 1 2 4 8 16 32 64 128
// 0 0 0 0 0  0  0  1

// time = O(logn)
// space = O(1)
