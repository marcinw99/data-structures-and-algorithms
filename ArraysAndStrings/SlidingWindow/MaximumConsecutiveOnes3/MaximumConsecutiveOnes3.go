package main

import "fmt"

func GetMaxConsecutiveOnes(nums []int, k int) int {
	left := 0

	currentZeroesCount := 0
	longestSubarrayLength := 0

	for right := 0; right < len(nums); right++ {
		if nums[right] == 0 {
			currentZeroesCount++
		}

		for currentZeroesCount > k {
			if nums[left] == 0 {
				currentZeroesCount--
			}
			left++
		}

		currentLength := right - left + 1

		longestSubarrayLength = max(currentLength, longestSubarrayLength)
	}

	return longestSubarrayLength
}

func main() {
	fmt.Println(GetMaxConsecutiveOnes([]int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}, 2))                         // 6
	fmt.Println(GetMaxConsecutiveOnes([]int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1}, 3)) // 10
	fmt.Println(GetMaxConsecutiveOnes([]int{0, 0, 0, 1}, 4))                                              // 4
}
