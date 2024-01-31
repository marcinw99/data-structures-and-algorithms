package main

import "fmt"

func GetRunningSum(nums []int) []int {
	result := nums

	for i, v := range result {
		if i > 0 {
			result[i] = result[i-1] + v
		}
	}

	return result
}

func main() {
	fmt.Println(GetRunningSum([]int{1, 2, 3, 4}))
}
