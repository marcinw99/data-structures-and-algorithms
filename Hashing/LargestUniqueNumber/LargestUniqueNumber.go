package main

import "fmt"

func largestUniqueNumber(nums []int) int {
	numsOccurrences := map[int]int{}

	for _, num := range nums {
		numsOccurrences[num]++
	}

	biggestBoi := -1

	for num, count := range numsOccurrences {
		if count == 1 && num > biggestBoi {
			biggestBoi = num
		}
	}

	return biggestBoi
}

func main() {
	fmt.Println(largestUniqueNumber([]int{5, 7, 3, 9, 4, 9, 8, 3, 1})) // 8
	fmt.Println(largestUniqueNumber([]int{9, 9, 8, 8}))                // -1
}
