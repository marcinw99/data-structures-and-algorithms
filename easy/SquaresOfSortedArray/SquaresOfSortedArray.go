package main

import "fmt"

func sortedSquares(nums []int) []int {
	numsLength := len(nums)

	leftIndex := 0
	rightIndex := numsLength - 1

	var squaredNums []int

	for leftIndex <= rightIndex {
		leftValue := nums[leftIndex] * nums[leftIndex]
		rightValue := nums[rightIndex] * nums[rightIndex]

		if leftValue > rightValue {
			squaredNums = append(squaredNums, leftValue)
			leftIndex++
		} else if leftValue < rightValue {
			squaredNums = append(squaredNums, rightValue)
			rightIndex--
		} else {
			squaredNums = append(squaredNums, rightValue)
			rightIndex--
		}
	}

	result := make([]int, numsLength)

	for i := range squaredNums {
		result[i] = squaredNums[numsLength-i-1]
	}

	return result
}

func sortedSquaresOptimised(nums []int) []int {
	numsLength := len(nums)

	leftIndex := 0
	rightIndex := numsLength - 1

	result := make([]int, numsLength)

	for i := numsLength - 1; i >= 0; i-- {
		leftValue := nums[leftIndex] * nums[leftIndex]
		rightValue := nums[rightIndex] * nums[rightIndex]

		if leftValue > rightValue {
			result[i] = leftValue
			leftIndex++
		} else {
			result[i] = rightValue
			rightIndex--
		}
	}

	return result
}

func main() {
	fmt.Println(sortedSquaresOptimised([]int{-4, -1, 0, 3, 10}))
	fmt.Println(sortedSquaresOptimised([]int{-1}))
}
