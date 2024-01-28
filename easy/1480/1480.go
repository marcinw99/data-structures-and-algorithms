package main

func main() {

}

func runningSum(nums []int) []int {
	result := nums
	for i, v := range nums {
		if i == 0 {
			result[0] = nums[0]
		} else {
			result[i] = v + nums[i-1]
		}
	}

	return result
}

// time = O(n)
// space = O(1)
