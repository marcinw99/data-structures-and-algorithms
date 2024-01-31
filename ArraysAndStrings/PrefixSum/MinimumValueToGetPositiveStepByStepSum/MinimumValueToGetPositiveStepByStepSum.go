package main

import "fmt"

func F(nums []int) int {
	prefix := nums
	lowestSum := nums[0]

	for i, v := range nums {
		if i > 0 {
			prefix[i] = prefix[i-1] + v

			if prefix[i] < lowestSum {
				lowestSum = prefix[i]
			}
		}
	}

	if lowestSum < 0 {
		return (lowestSum * -1) + 1
	}

	return 1
}

func FButSimpler(nums []int) int {
	currentSum := nums[0]
	lowestSum := nums[0]

	for i, v := range nums {
		if i > 0 {
			currentSum += v
			lowestSum = min(currentSum, lowestSum)
		}
	}

	if lowestSum < 0 {
		return (lowestSum * -1) + 1
	}

	return 1
}

func main() {
	//fmt.Println(F([]int{-3, 2, -3, 4, 2})) // 5
	fmt.Println(FButSimpler([]int{-3, 2, -3, 4, 2})) // 5
}
