package main

import "fmt"

func getCountOfSubarraysWithProductLessThanK(nums []int, k int) int {
	if k <= 1 {
		return 0
	}

	answer := 0
	left := 0
	current := 1

	for right, rightValue := range nums {
		current *= rightValue

		for current >= k {
			current /= nums[left]
			left++
		}

		answer += right - left + 1
	}

	return answer
}

func main() {
	//testData := []int{10, 10, 10, 6}
	//testData := []int{100, 100, 100, 6}
	testData := []int{10, 5, 2, 6}

	fmt.Println(getCountOfSubarraysWithProductLessThanK(testData, 100))
}
