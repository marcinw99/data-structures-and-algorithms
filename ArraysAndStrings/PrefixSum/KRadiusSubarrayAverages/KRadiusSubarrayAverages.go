package main

import "fmt"

func F(nums []int, k int) []int {
	prefix := nums

	averages := make([]int, len(nums))

	for i, v := range nums {
		if i > 0 {
			prefix[i] = prefix[i-1] + v
		}
	}

	for i := range averages {
		if i >= k && i < len(averages)-k {
			var sumForCurrentRadius int
			if i == k {
				sumForCurrentRadius = prefix[i+k]
			} else {
				sumForCurrentRadius = prefix[i+k] - prefix[i-k-1]
			}
			averages[i] = sumForCurrentRadius / ((2 * k) + 1)
		} else {
			averages[i] = -1
		}
	}

	return averages
}

func main() {
	fmt.Println(F([]int{7, 4, 3, 9, 1, 8, 5, 2, 6}, 3)) // [-1,-1,-1,5,4,4,-1,-1,-1]
	fmt.Println(F([]int{100000}, 0))                    // [100 000]
	fmt.Println(F([]int{8}, 100000))                    // [-1]
}
