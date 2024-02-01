package main

import (
	"fmt"
	"slices"
)

func missingNumber(nums []int) int {
	n := len(nums) + 1
	allNumbersFromN := make([]int, n)

	for i := 1; i < n; i++ {
		allNumbersFromN[i] = i
	}

	for _, v := range allNumbersFromN {
		if !slices.Contains(nums, v) {
			return v
		}
	}

	return -1
}

// T = O(n), S = O(n)

func missingNumberBetter(nums []int) int { // Gauss formula / suma ciągu arytmetycznego
	n := len(nums) + 1
	remainingTotal := (n * (n - 1)) / 2

	for _, v := range nums {
		remainingTotal -= v
	}

	return remainingTotal
}

// T = O(n), S = O(1)

func missingNumberFirstButSimpler(nums []int) int {
	for i := 0; i < len(nums); i++ {
		if !slices.Contains(nums, i) { // usually we should make it as Set so that we can query for containment in O(1)
			return i
		}
	}

	return -1
}

func main() {
	//fmt.Println(missingNumber([]int{3, 0, 1}))
	fmt.Println(missingNumberFirstButSimpler([]int{3, 0, 1}))
	//fmt.Println(missingNumberBetter([]int{3, 0, 1}))
}
