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

func largestUniqueNumberCountingSort(A []int) int {
	count := make([]int, 1001)
	for _, n := range A {
		count[n]++
	}

	for i := len(count) - 1; i >= 0; i-- {
		if count[i] == 1 {
			return i
		}
	}

	return -1
}
