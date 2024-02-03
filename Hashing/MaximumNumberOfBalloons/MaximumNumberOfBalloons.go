package main

import "fmt"

func maxNumberOfBalloons(text string) int {
	accumulatedLetters := map[int32]int{}

	for _, letter := range text { // O(n)
		accumulatedLetters[letter]++
	}

	targetString := "balloon"
	requiredLettersAmountPerOccurrence := map[int32]int{}

	for _, letter := range targetString { // O(1)
		requiredLettersAmountPerOccurrence[letter]++
	}

	lowestCount := -1
	for letter, amount := range requiredLettersAmountPerOccurrence { // O(1)
		count := accumulatedLetters[letter] / amount

		if lowestCount == -1 || count < lowestCount {
			lowestCount = count
		}
	}

	return lowestCount
}

// T = S = O(n)

func main() {
	fmt.Println(maxNumberOfBalloons("nlaebolko"))        // 1
	fmt.Println(maxNumberOfBalloons("loonbalxballpoon")) // 2
	fmt.Println(maxNumberOfBalloons("leetcode"))         // 0
	fmt.Println(maxNumberOfBalloons("balon"))            // 0
}
