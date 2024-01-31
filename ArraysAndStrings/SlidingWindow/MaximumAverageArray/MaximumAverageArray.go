package main

import "fmt"

func GetMaximumAverageArray(nums []int, k int) float64 {
	initialSum := 0

	for i := 0; i < k; i++ {
		initialSum += nums[i]
	}

	currentSum := initialSum
	answer := float64(currentSum) / float64(k)

	left := 0

	for right := k; right <= len(nums)-1; right++ {
		currentSum += nums[right]
		currentSum -= nums[left]

		newAverage := float64(currentSum) / float64(k)

		if newAverage > answer {
			answer = newAverage
		}

		left++
	}

	return answer
}

func GetMaximumAverageArraySimplified(nums []int, k int) float64 {
	initialSum := 0

	for i := 0; i < k; i++ {
		initialSum += nums[i]
	}

	currentSum := initialSum
	biggestSum := currentSum

	left := 0

	for right := k; right < len(nums); right++ {
		currentSum += nums[right] - nums[left]

		biggestSum = max(currentSum, biggestSum)

		left++
	}

	return float64(biggestSum) / float64(k)
}

func main() {
	//fmt.Println(GetMaximumAverageArray([]int{1, 12, -5, -6, 50, 3}, 4))
	fmt.Println(GetMaximumAverageArraySimplified([]int{1, 12, -5, -6, 50, 3}, 4))
}
