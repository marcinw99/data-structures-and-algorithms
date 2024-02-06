package main

import "fmt"

// mine, works but too slow
func findMaxLength(nums []int) int {
	prefix := make([]int, len(nums))
	prefix[0] = nums[0]

	answer := 0

	// from 1 since no valid subarrays can be at 0
	for i := 1; i < len(nums); i++ {
		prefix[i] = nums[i] + prefix[i-1]
		furthestIndex := (prefix[i] * 2) - i - 1

		for j := furthestIndex; j < i && i-j+1 > answer; j++ {
			sum := prefix[i]
			if j > 0 { // the whole array can also be valid - no need for prefix sum formula
				sum -= prefix[j-1]
			}
			length := i - j + 1
			if sum*2 == length {
				answer = max(answer, length)
			}
		}
	}

	return answer
}

// poor attempt to improve the above
func findMaxLengthOptimised(nums []int) int {
	prefix := make([]int, len(nums))
	prefix[0] = nums[0]

	for i := 1; i < len(nums); i++ {
		prefix[i] = nums[i] + prefix[i-1]
	}

	answer := 0

	for i := len(prefix) - 1; i >= 0; i-- {

		furthestIndex := (prefix[i] * 2) - i - 1

		for j := furthestIndex; j < i && i-j+1 > answer; j++ {
			sum := prefix[i]
			if j > 0 { // the whole array can also be valid - no need for prefix sum formula
				sum -= prefix[j-1]
			}
			length := i - j + 1
			if sum*2 == length {
				answer = max(answer, length)
			}
		}
	}

	return answer
}

// all below from LC
func findMaxLengthLast(nums []int) int {
	answer := 0
	current := 0
	indexesPerSum := map[int][]int{}

	for i, num := range nums {
		if num == 0 {
			current -= 1
		} else {
			current += 1
		}

		if _, ok := indexesPerSum[current]; ok {
			indexesPerSum[current] = append(indexesPerSum[current], i)
		} else {
			indexesPerSum[current] = []int{current}
		}
	}

	fmt.Println(indexesPerSum)

	return answer
}

func main() {
	//fmt.Println(findMaxLengthLast([]int{0, 1}))                   // 2
	//fmt.Println(findMaxLengthLast([]int{0, 1, 0}))                // 2
	//fmt.Println(findMaxLengthLast([]int{0, 1, 0, 1}))       // 4
	fmt.Println(findMaxLengthLast([]int{0, 0, 1, 0}))             // 2
	fmt.Println(findMaxLengthLast([]int{0, 0, 0, 1, 1, 0, 0, 0})) // 4
	//fmt.Println(findMaxLengthLast([]int{0, 0, 0, 1, 1, 1})) // 6
	fmt.Println(findMaxLengthLast([]int{1, 1, 1, 0, 0, 0})) // 6
	fmt.Println(findMaxLengthLast([]int{1, 1, 1, 1, 0, 0})) // 4
	//fmt.Println(findMaxLengthLast([]int{0, 0, 0, 0}))             // 0
	fmt.Println(findMaxLengthLast([]int{0, 0, 1, 0, 0, 0, 1, 1})) // 6
	//testData := []int{1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1}
	//fmt.Println(findMaxLengthLast(testData)) // 94 (from 6 to 100)
}
