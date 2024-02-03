package main

import "fmt"

// this code doesn't always work and is most likely more complicated than it should be
func findMaxLength(nums []int) int {
	answer := 0

	prefix := make([]int, len(nums))

	for i, num := range nums {
		if i == 0 {
			prefix[0] = num
		} else {
			prefix[i] = num + prefix[i-1]
		}
	}

	// find the longest subarray which sum is equal to half of its length

	for i := 0; i <= len(prefix)-1; i++ {
		furthestPotentialStart := i - (prefix[i]*2 - 1)
		if i > 0 && furthestPotentialStart >= 0 {
			sum := prefix[i]
			if furthestPotentialStart > 0 { // sometimes we take full array into account
				sum -= prefix[furthestPotentialStart-1]
			}
			length := i - furthestPotentialStart + 1
			if sum*2 == length {
				answer = max(answer, length)
			}
		}
	}

	return answer
}

func main() {
	//fmt.Println(findMaxLength([]int{0, 1}))                   // 2
	//fmt.Println(findMaxLength([]int{0, 1, 0}))                // 2
	//fmt.Println(findMaxLength([]int{0, 1, 0, 1}))             // 4
	//fmt.Println(findMaxLength([]int{0, 0, 1, 0}))             // 2
	//fmt.Println(findMaxLength([]int{0, 0, 0, 1, 1, 1}))       // 6
	//fmt.Println(findMaxLength([]int{1, 1, 1, 0, 0, 0}))       // 6
	//fmt.Println(findMaxLength([]int{0, 0, 0, 0}))             // 0
	//fmt.Println(findMaxLength([]int{0, 0, 1, 0, 0, 0, 1, 1})) // 6
	fmt.Println(findMaxLength([]int{1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1})) // 94
}
